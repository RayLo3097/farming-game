import geocoder # For obtaining the user's approximate location
import openmeteo_requests # For getting weather data
import requests_cache
import pandas as pd
from retry_requests import retry
from classes.weatherdata import WeatherData

class RealWeather:
    # For determining the data to obtain
    __latitude: float
    __longitude: float

    # Weather Data
    __lastUpdate: pd.Timestamp  # Timestamp of the last weather update
    __weatherNow: WeatherData   # The weather right now (some parts are only the last hour)
    __weatherToday: WeatherData # The weather expected for the day

    __weatherPrev: WeatherData  # The weather of the recent past
    __weatherNext: WeatherData  # The weather of the soon future

    def __init__(self, lat: float = None, long: float = None, lastUpdate: pd.Timestamp = None):
        # If latitude/longitude are not given
        if lat == None or long == None:
            geo_temp = geocoder.ip('me') # Get lat/long by IP
            [temp_lat, temp_long] = geo_temp.latlng
            self.__latitude = temp_lat
            self.__longitude = temp_long
        else:
            self.__latitude = lat
            self.__longitude = long

        self.__lastUpdate = lastUpdate

    def getLatLong(self):
        return (self.__latitude, self.__longitude)

    def getWeatherNow(self):
        return self.__weatherNow

    def getWeatherPrev(self):
        return self.__weatherPrev

    def getWeatherToday(self):
        return self.__weatherToday

    def getWeatherNext(self):
        return self.__weatherNext

    def requestWeather(self):
        ###############################
        # Setup - Open-Meteo API Call #
        ###############################

        # If a request was sent too recently, pull from cache to prevent unnecessary calls
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)

        # Retry request if it failed for whatever reason
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)

        # The API Client
        openmeteo = openmeteo_requests.Client(session = retry_session)

        # Parameters we always use when making a request to the API
        params = {
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "current": ["apparent_temperature", "precipitation", "weather_code", "cloud_cover"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timeformat": "unixtime"
        }

        """
            Update Flag

            If this is the first request / no data has been loaded into the class
            OR
            The date of the last update and the date of the current data are not the same,
            THEN
            We get both previous weather and predicted next weather
        """
        updatePrevNext_flag = (self.__lastUpdate == None)
        if not updatePrevNext_flag:
            # If __lastUpdate has a value, check if an update is needed
            updatePrevNext_flag = not (self.__lastUpdate.date() == self.__weatherNow.timestamp.date())

        if updatePrevNext_flag:
            # Updating the api parameter dictionary to have the necessary data points and time ranges requested
            params['daily'] = ["weather_code", "apparent_temperature_max", "apparent_temperature_min", "precipitation_sum", "precipitation_probability_max"]
            params['past_days'] = 4 # We do 4 days in the past, because the API includes today as the past
            params['forecast_days'] = 3

        # Making the API call
        responses = openmeteo.weather_api('https://api.open-meteo.com/v1/forecast', params=params)
        response = responses[0] # Only one coordinate is requested, so only the first response is needed

        #########################
        #    CURRENT WEATHER    #
        #########################

        resCurrent = response.Current()                     #  Getting "Current" data requested from API
        latestWeatherData = WeatherData(
            ts = pd.Timestamp(resCurrent.Time(), unit='s'), #  Converting time (in seconds) to Timestamp type
            temp = int(resCurrent.Variables(0).Value()),    #  Current Temperature
            tempL = None,                                   #* We do not use this for current weather data
            tempH = None,                                   #* We do not use this for current weather data
            code = resCurrent.Variables(2).Value(),         #  Weather Code describing current weather
            rain = resCurrent.Variables(1).Value(),         #  Amount of rain in the last hour #!! Just use this to determine if it is "currently" raining
            cover = resCurrent.Variables(3).Value()         #  The amount of cloud coverage right now, as a percentage
        )

        # Set class attribute
        self.__weatherNow = latestWeatherData

        ###########################
        #    DAY-BASED WEATHER    #
        ###########################

        resDaily = response.Daily() # Getting "Daily" data requested from API

        # Easier access to requested data
        daysWeatherCode = resDaily.Variables(0).ValuesAsNumpy()
        daysTempMax = resDaily.Variables(1).ValuesAsNumpy()
        daysTempMin = resDaily.Variables(2).ValuesAsNumpy()
        daysPrecipSum = resDaily.Variables(3).ValuesAsNumpy()
        daysPrecipProb = resDaily.Variables(4).ValuesAsNumpy()

        # If not updating __previousWeather and __nextWeather
        if not updatePrevNext_flag:
            return

        # Date range we requested
        datetimes = pd.date_range(
            start = pd.to_datetime(resDaily.Time(), unit = "s"),
            end = pd.to_datetime(resDaily.TimeEnd(), unit = "s"),
            freq = pd.Timedelta(seconds = resDaily.Interval()),
            inclusive = "left"
        ).tolist()

        #########################
        #   PREVIOUS WEATHER    #
        #########################

        # Store the previous three (3) days of weather
        self.__weatherPrev = []
        for i in range(0, 3):
            self.__weatherPrev.append(WeatherData(
                ts = datetimes[i],               #  Date of the weather data
                # temp = None,                   #* Not provided by the API
                tempL = daysTempMin[i],          #  Low Temperature of the day
                tempH = daysTempMax[i],          #  High Temperature of the day
                code = daysWeatherCode[i],       #  Weather Code for the day
                rain = daysPrecipSum[i],         #  Amount of rain for that day [technically also counts snow as rain]
                precipChance = daysPrecipProb[i] #  Chance of precipitation (rain/snow) #!! may not apply to previous days
                # cover = 0,                     #* Not provided by the API
            ))

        #############################
        # TODAY'S PREDICTED WEATHER #
        #############################

        self.__weatherToday = WeatherData(
            ts = datetimes[i],               #  Today's Date
            # temp = None,                   #* We obtain this from current weather
            tempL = daysTempMin[i],          #  Low Temperature of the day
            tempH = daysTempMax[i],          #  High Temperature of the day
            code = daysWeatherCode[i],       #  Weather Code for the day
            rain = daysPrecipSum[i],         #  Amount of rain for that day [technically also counts snow as rain] #!! Not sure if we even need this
            precipChance = daysPrecipProb[i] #  Chance of precipitation (rain/snow)
            # cover = 0,                     #* We obtain this from current weather
        )

        ##########################
        # PREDICTED NEXT WEATHER #
        ##########################

        # Store the next three (3) days of predicted weather
        self.__weatherNext = []
        for i in range(4, 7):
            self.__weatherNext.append(WeatherData(
                ts = datetimes[i],               #  Date of the weather data
                # temp = None,                   #* Not provided by the API
                tempL = daysTempMin[i],          #  Low Temperature of the day
                tempH = daysTempMax[i],          #  High Temperature of the day
                code = daysWeatherCode[i],       #  Weather Code for the day
                rain = daysPrecipSum[i],         #  Amount of rain for that day [technically also counts snow as rain]
                precipChance = daysPrecipProb[i] #  Chance of precipitation (rain/snow)
                # cover = 0,                     #* Not provided by the API
            ))

        self.__weatherNow.printToConsole()


    # def requestHistoricalWeather(self, start: datetime, end: datetime):
        # may need to set a limit on how far back this can go






