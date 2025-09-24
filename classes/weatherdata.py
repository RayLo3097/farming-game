import pandas

"""
    timestamp       : date and time of the given weather data
    temperature     : current temperature, in fahrenheit
    temperatureLow  : predicted or historic low temperature of the day, in fahrenheit
    temperatureHigh : predicted or historic high temperature of the day, in fahrenheit
    weatherCode     : WMO weather code to describe conditions (to be used to determine if raining)
    rainInches      : amount of rain in a given day, or the last hour (we treat this as current), in inches
    cloudCoverage   : cloud coverage for a given day, or the last hour (we treat this as current), as a percentage [0.0, 100.0]
"""
class WeatherData:
    timestamp: pandas.Timestamp
    temperature: int
    temperatureLow: int
    temperatureHigh: int
    precipitationProbability: float
    weatherCode: int # Refer to WMO Code Table
    rainInches: int
    cloudCoverage: int

    def __init__(self, ts: pandas.Timestamp, temp: int = None, tempL: int = None, tempH: int = None,
                 code: int = -1, precipChance: float = 0.0, rain: int = 0.0, cover: float = 0.0):
        self.timestamp = ts
        self.temperature = temp
        self.temperatureLow = tempL
        self.temperatureHigh = tempH
        self.weatherCode = code
        self.precipitationProbability = precipChance
        self.rainInches = rain
        self.cloudCoverage = cover
    
    def printToConsole(self):
        out = f'{self.timestamp}:'
        out += f'\n\tCurrent Temperature: {self.temperature}'
        out += f'\n\tLow/High Temp: {self.temperatureLow}/{self.temperatureHigh}'
        out += f'\n\tWeather Code: {self.weatherCode}'
        out += f'\n\tPrecipitation Chance: {self.precipitationProbability}%'
        out += f'\n\tRain: {self.rainInches} inches'
        out += f'\n\tCloud Coverage: {self.cloudCoverage}%'
        print(out)