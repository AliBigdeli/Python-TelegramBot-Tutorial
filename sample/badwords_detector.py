import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

bad_word_list = ["badword1","badword2","badword3"]

warnings = {}

def has_bad_words(text):
    for bad_word in bad_word_list:
        if bad_word in text:
            return True
    return False

@bot.message_handler(func=lambda message:True)
def message_handler(message):
    if str(message.from_user.id) in warnings:
        warnings[str(message.from_user.id)] +=1
    else:
        warnings[str(message.from_user.id)] =1
    
    if warnings[str(message.from_user.id)] > 3:
        bot.kick_chat_member(message.chat.id,message.from_user.id)
        bot.send_message(message.chat.id,f"user {message.from_user.username} has been kicked out because of breaking bad word rule" )
    else:
        bot.reply_to(message,f"please dont use bad words, this is your {warnings[str(message.from_user.id)]} warnings, after third warning you will be kicked out")
    

bot.infinity_polling()