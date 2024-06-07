import telebot
import os
import logging
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info(message.chat.__dict__)
    bot.send_message(message.chat.id, """Hi this is a sample for learning telegram bot in python""")


        
bot.infinity_polling()







