from time import sleep
import telebot
from ApiCallService import ApiCallService

bot = telebot.TeleBot('896808497:AAH492edFi5DVVmciFHvAKJXqoGniQRyreY')
api_call_service = ApiCallService()

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Hello! \n Send me your city to get weather forecast')

@bot.message_handler(func=lambda msg: msg.text is not None)
def get_weather_forecast(message):
    response = api_call_service.weather_by_city_name(message.text)

    bot.reply_to(message,response)

while True:
    try:
        bot.polling()
    except Exception:
        sleep(15)

