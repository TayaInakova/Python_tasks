#  Написать парсер чего-нибудь
import requests
from bs4 import BeautifulSoup as bs

# Адрес Центрального Банка
url = 'https://cbr.ru'
response = requests.get(url).text
soup = bs(response, 'html.parser')
address_of_bank = soup.find('div', class_="footer_address").text
print(address_of_bank)

# Погода в Москве
url = 'https://pogoda.mail.ru/prognoz/moskva/'
response = requests.get(url).text
soup = bs(response, 'html.parser')
temperature = soup.find('div', class_="information__content__temperature").text
fill_temperature = soup.find('div', class_="information__content__additional__item").find('span').text
precipitation = soup.find('div', class_="information__content__additional information__content__additional_first").find(
    'div', class_='information__content__additional__item').text
temperature = temperature.replace('\n', '')
temperature = temperature.replace('\t', '')
fill_temperature = fill_temperature.replace('\n', '')
fill_temperature = fill_temperature.replace('\t', '')
precipitation = precipitation.replace('\n', '')
precipitation = precipitation.replace('\t', '')
print(f'Погода: {temperature}, {fill_temperature}, {precipitation}')
