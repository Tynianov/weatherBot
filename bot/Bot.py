from time import sleep
from telebot import TeleBot
from flask import Flask, request
import os
from ApiCallService import ApiCallService

TOKEN = '896808497:AAH492edFi5DVVmciFHvAKJXqoGniQRyreY'
bot = TeleBot(TOKEN)
api_call_service = ApiCallService()
server = Flask(__name__)

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

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://nameless-mesa-97442.herokuapp.com/' + TOKEN)
    return "!", 200
