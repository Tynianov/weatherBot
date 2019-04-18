from requests import get, exceptions

API_KEY = 'd31fd3af0ed000ee05bb658aaf5fb6b3'

class ApiCallService:

    def __init__(self):
        self.params = {
                'appid': 'd31fd3af0ed000ee05bb658aaf5fb6b3',
                'units': 'metric'
             }

    def weather_by_city_name(self,city):
        self.params['q'] = city

        try:
            request = get('http://api.openweathermap.org/data/2.5/weather',params=self.params)
            return self.format_output(request.json())
        except exceptions.InvalidURL:
            return 'Sorry, your city name is incorrect!'

    def format_output(self,json_response):

        return 'Current weather forecast for {}:' \
               '{}, {}\n' \
               'Temperature: {} Celsius\n' \
               'Atmospheric pressure: {} hPa\n' \
               'Humidity: {} %\n' \
               'Wind speed: {} meter/sec'.format(json_response['name'],json_response['weather'][0]['main'],
                                                 json_response['weather'][0]['description'], json_response['main']['temp'],
                                                 json_response['main']['pressure'],json_response['main']['humidity'],
                                                 json_response['wind']['speed'])
