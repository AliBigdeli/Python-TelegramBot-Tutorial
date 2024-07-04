import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

CHANNEL_ID = "YOUR_CHANNEL_ID"
CHANNEL_LINK = "YOUR_CHANNEL_LINK"

def is_member(message):
    user_info = bot.get_chat_member(CHANNEL_ID,message.from_user.id)
    if not user_info.status in ["administrator","creator","member"]:
        bot.send_message(message.chat.id,f"please subscribe to our channel so you can use this bot: [Join Channel]({CHANNEL_LINK})",parse_mode="Markdown")
        return False
    return True


@bot.message_handler(func=lambda message:True)
def message_handler(message):
    bot.reply_to()

bot.infinity_polling()