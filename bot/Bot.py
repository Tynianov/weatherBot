from time import sleep
import telebot
from ApiCallService import ApiCallService

bot = telebot.TeleBot('896808497:AAH492edFi5DVVmciFHvAKJXqoGniQRyreY')
api_call_service = ApiCallService()

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Hello! \n Send me your city to get weather forecast')

@bot.message_handler(commands=['current_weather'])
def get_current_weather(message):
    msg = bot.reply_to(message,"Ok!\nEnter your city please")
    bot.register_next_step_handler(msg,process_city)

def process_city(message):
    response = api_call_service.weather_by_city_name(message.text)

    bot.send_message(message.chat.id, response)


while True:
    try:
        bot.polling()
    except Exception:
        sleep(15)

