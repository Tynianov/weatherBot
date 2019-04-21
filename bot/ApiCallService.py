from requests import get, exceptions
from emoji import emojize

API_KEY = 'd31fd3af0ed000ee05bb658aaf5fb6b3'

class ApiCallService:

    def __init__(self):
        self.params = {
                'appid': 'd31fd3af0ed000ee05bb658aaf5fb6b3',
                'units': 'metric'
             }

    def weather_by_city_name(self,city):

        # try:
        self.params['q'] = city
        request = get('http://api.openweathermap.org/data/2.5/weather',params=self.params)
        return self.format_output(request.json())
        # except Exception:
        #     return 'Sorry, your city name is incorrect!'

    def format_output(self,json_response):

        return 'Current weather forecast for {}\n' \
               '{} {}, {}\n' \
               '{} Temperature: {} Celsius\n' \
               '{} Atmospheric pressure: {} hPa\n' \
               '{} Humidity: {} %\n' \
               '{} Wind speed: {} meter/sec\n' \
               '{} Cloudiness: {} %'.format(json_response['name'],self.get_emoji_by_weather(json_response['weather'][0]['main']),
                                         json_response['weather'][0]['main'],json_response['weather'][0]['description'],emojize(':thermometer:'),
                                         json_response['main']['temp'],emojize(':cyclone:'),json_response['main']['pressure'],
                                         emojize(':droplet:'), json_response['main']['humidity'],
                                         emojize(':wind_face:'),json_response['wind']['speed'],
                                         emojize(':cloud:'),json_response['clouds']['all'])


    def get_emoji_by_weather(self,weather_condition):

        if weather_condition == 'Thunderstorm':
            return emojize(':thunder_cloud_and_rain:')
        elif weather_condition == 'Drizzle':
            return emojize(':white_sun_behind_cloud_with_rain:')
        elif weather_condition == 'Snow':
            return emojize(':snowflake:')
        elif weather_condition == 'Rain':
            return emojize(':cloud_with_rain:')
        elif weather_condition == 'Clear':
            return emojize(':sun:')
        elif weather_condition == 'Clouds':
            return emojize(':cloud:')
        elif weather_condition == 'Tornado':
            return emojize(':tornado:')
        elif weather_condition == 'Fog':
            return emojize(':fog:')
        else:
            return ''
