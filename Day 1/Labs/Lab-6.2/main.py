from openweathermap import getforecast, getcurrentweather

# List of city ID city.list.json.gz can be downloaded here
# http://bulk.openweathermap.org/sample/

#CityID='Put your CityID here'
CityID='2960316'

#APIKey='Put YOUR API KEY here'

print("\nGeting current weather")
country,city,temp, temp_min, temp_max, short_weather, long_weather = getcurrentweather(CityID, APIKey)
print("Current weather for {}, {}: {}°C, {}".format(city, country, temp, long_weather))
print("min {}, max {} ".format(temp_min, temp_max))

print('\nRetrieving the weather forecast')
country, city, short_forecast, long_forecast, temp, humidity = getforecast(CityID, APIKey)
print("Tomorrow's forecast: {}, {}°C - {}% humidity\n".format(long_forecast, temp, humidity))
