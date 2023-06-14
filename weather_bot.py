import telebot
import requests
import datetime

TOKEN = '5666835397:AAHOkCbP9r4FsIz8-EpDZx_7gY-9X8SY4W4'

bot = telebot.TeleBot(TOKEN)


def get_weather_forecast():
    api_key = 'b18b499fdc9f46fc85e131405231306'

    lat = 'Perm'

    url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat}&days=1&aqi=no&alerts=no'

    response = requests.get(url)
    data = response.json()

    forecast_date = data['forecast']['forecastday'][0]['date']
    forecast_degree = data['forecast']['forecastday'][0]['day']['avgtemp_c']
    forecast_condition = data['forecast']['forecastday'][0]['day']['condition']['text']
    forecast_avghumidity = data['forecast']['forecastday'][0]['day']['avghumidity']

    return f'Прогноз погоды на {forecast_date}: \n' \
           f'Температура: {forecast_degree} °C \n' \
           f'Состояние погоды: {forecast_condition} \n' \
           f'Средняя влажность: {forecast_avghumidity}%'


def get_tomorrow_weather_forecast():
    api_key = 'b18b499fdc9f46fc85e131405231306'

    lat = 'Perm'

    url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat}&days=2&aqi=no&alerts=no'

    response = requests.get(url)
    data = response.json()

    forecast_date = data['forecast']['forecastday'][1]['date']
    forecast_degree = data['forecast']['forecastday'][1]['day']['avgtemp_c']
    forecast_condition = data['forecast']['forecastday'][1]['day']['condition']['text']
    forecast_avghumidity = data['forecast']['forecastday'][1]['day']['avghumidity']

    return f'Прогноз погоды на {forecast_date}: \n' \
           f'Температура: {forecast_degree} °C \n' \
           f'Состояние погоды: {forecast_condition} \n' \
           f'Средняя влажность: {forecast_avghumidity}%'


def get_hourly_forecast():
    api_key = 'b18b499fdc9f46fc85e131405231306'

    lat = 'Perm'

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat}&aqi=no'

    response = requests.get(url)
    data = response.json()

    forecast_date = data['location']['localtime']
    forecast_degree = data['current']['temp_c']
    forecast_condition = data['current']['condition']['text']
    forecast_humidity = data['current']['humidity']

    return f'Прогноз погоды на {forecast_date}: \n' \
           f'Температура: {forecast_degree} °C \n' \
           f'Состояние погоды: {forecast_condition} \n' \
           f'Влажность: {forecast_humidity}%'


def get_weekly_forecast():
    api_key = 'b18b499fdc9f46fc85e131405231306'

    lat = 'Perm'

    url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat}&days=10&aqi=no&alerts=no'

    response = requests.get(url)
    data = response.json()

    forecast = ''

    for i in range(7):
        forecast_date = data['forecast']['forecastday'][i]['date']
        forecast_degree = data['forecast']['forecastday'][i]['day']['avgtemp_c']
        forecast_condition = data['forecast']['forecastday'][i]['day']['condition']['text']
        forecast_avghumidity = data['forecast']['forecastday'][i]['day']['avghumidity']

        forecast += f'Прогноз погоды на {forecast_date}: \n' \
                    f'Температура: {forecast_degree} °C \n' \
                    f'Состояние погоды: {forecast_condition} \n' \
                    f'Средняя влажность: {forecast_avghumidity}% \n\n'

    return forecast


def get_astronomy_data():
    api_key = 'b18b499fdc9f46fc85e131405231306'

    lat = 'Perm'

    url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat}&days=1&aqi=no&alerts=no'

    response = requests.get(url)
    data = response.json()

    sunrise = data['forecast']['forecastday'][0]['astro']['sunrise']
    sunset = data['forecast']['forecastday'][0]['astro']['sunset']

    return sunrise, sunset


@bot.message_handler(commands=['forecast'])
def send_weather_forecast(message):
    forecast = get_weather_forecast()
    bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['weekly'])
def send_weekly_forecast(message):
    forecast = get_weekly_forecast()
    bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['tomorrow'])
def send_tomorrow_weather_forecast(message):
    forecast = get_tomorrow_weather_forecast()
    bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['astronomy'])
def send_astronomy_data(message):
    sunrise, sunset = get_astronomy_data()
    response = 'Астрономические данные для Перми: \n'
    response += f'Время восхода: {sunrise} \n'
    response += f'Время заката: {sunset}'
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['hourly'])
def send_hourly_forecast_request(message):
    forecast = get_hourly_forecast()
    bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для получения информации о погоде. Выберите одну из команд: \n'
                                      '/forecast - прогноз погоды \n'
                                      '/tomorrow - прогноз погоды на завтра \n'
                                      '/weekly - прогноз погоды на неделю \n'
                                      '/astronomy - астрономические данные \n'
                                      '/hourly - прогноз на определенный час')


bot.polling()
