import requests

API_KEY = 'your_openweathermap_api_key'
CITY = 'your_city_name'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

weather_data = get_weather_data(CITY)
print(weather_data)