import pandas as pd
import pytest
from io import StringIO
from contextlib import redirect_stdout
from classes.weatherdata import WeatherData

# Fixture for creating a WeatherData object
@pytest.fixture
def weather_data():
    timestamp = pd.Timestamp('2022-01-01 12:00')
    return WeatherData(
        ts=timestamp,
        temp=70,
        tempL=65,
        tempH=75,
        code=100,
        precipChance=50.0,
        rain=0.1,
        cover=40.0
    )

# Test initialization
def test_weather_data_initialization(weather_data):
    assert weather_data.timestamp == pd.Timestamp('2022-01-01 12:00')
    assert weather_data.temperature == 70
    assert weather_data.temperatureLow == 65
    assert weather_data.temperatureHigh == 75
    assert weather_data.weatherCode == 100
    assert weather_data.precipitationProbability == 50.0
    assert weather_data.rainInches == 0.1
    assert weather_data.cloudCoverage == 40.0

# Test the printToConsole method
def test_weather_data_print_to_console(weather_data):
    f = StringIO()
    with redirect_stdout(f):
        weather_data.printToConsole()
    out = f.getvalue()
    assert "Current Temperature: 70" in out
    assert "Low/High Temp: 65/75" in out
    assert "Weather Code: 100" in out
    assert "Precipitation Chance: 50.0%" in out
    assert "Rain: 0.1 inches" in out
    assert "Cloud Coverage: 40.0%" in out

# Test initialization with None values
def test_weather_data_initialization_none(weather_data):
    timestamp = pd.Timestamp('2022-01-01 12:00')
    weather_data_none = WeatherData(
        ts=timestamp,
        temp=None,
        tempL=None,
        tempH=None,
        code=None,
        precipChance=None,
        rain=None,
        cover=None
    )
    assert weather_data_none.temperature is None
    assert weather_data_none.temperatureLow is None
    assert weather_data_none.temperatureHigh is None
    assert weather_data_none.weatherCode is None
    assert weather_data_none.precipitationProbability is None
    assert weather_data_none.rainInches is None
    assert weather_data_none.cloudCoverage is None