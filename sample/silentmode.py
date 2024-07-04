import telebot
import os
import logging
from telebot.types import ChatPermissions

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

def is_admin(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    user_info = bot.get_chat_member(chat_id,user_id)
    return user_info.status in ["creator","administrator"]

@bot.message_handler(func=is_admin,commands=["restrict"])
def handle_restriction(message):
    permissions = ChatPermissions(
        can_send_messages =False
    )
    bot.set_chat_permissions(message.chat.id,permissions=permissions)
    bot.delete_message(message.chat.id,message.message.id)
    bot.send_message(message.chat.id,"night mode activated")
    logger.info("applying restriction")
    

@bot.message_handler(func=is_admin,commands=["unrestrict"])
def handle_restriction(message):
    permissions = ChatPermissions(
        can_send_messages =True
    )
    bot.set_chat_permissions(message.chat.id,permissions=permissions)
    bot.delete_message(message.chat.id,message.message.id)
    bot.send_message(message.chat.id,"night mode deactivated")
    logger.info("applying unrestriction")


 
bot.infinity_polling()