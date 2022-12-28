
#  Написать парсер чего-нибудь

import requests

API_key = '3c5e466be166547ac88a15cc126e5235'
city_name = 'Тула'  # input('Введите название города: ')
response = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru')
weather = response.json()
# print(weather)
weather_temp = response.json()['main']['temp']
weather_temp_feels = response.json()['main']['feels_like']
# weather_cloud = response.json()['weather']['id']
print(
    f'В городе {city_name} {weather_temp} градусов.\nОщущается как {weather_temp_feels}\n'
    f'')
# Облачность - {weather_cloud}

