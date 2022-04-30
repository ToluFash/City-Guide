"""
Uses the OpenWeatherMap API (Reference: https://openweathermap.org)

Current city weather API reference doc: https://openweathermap.org/current
Weather forecast API reference doc: https://openweathermap.org/forecast16
"""
import os

OPEN_WEATHER_API_KEY = "c11441c1fbd45adaec96f8ddd8d5b82b" #os.environ.get("OPEN_WEATHER_API", "")

OPEN_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID=" + OPEN_WEATHER_API_KEY
OPEN_FORECAST_API_URL = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&cnt={1}&APPID=" + \
                        OPEN_WEATHER_API_KEY
