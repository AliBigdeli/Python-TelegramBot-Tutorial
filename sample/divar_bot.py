import telebot
import os
import logging
import requests

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "لطفا کلید واژه مورد نظر خود برای سرچ در دیوار را وارد نمایید")

def fetch_divar_ads(text_query):
    url = "https://api.divar.ir/v8/web-search/karaj"
    params = {
        "q":text_query
    }
    response = requests.get(url=url,params=params)
    return response.json()

 
@bot.message_handler(func=lambda message:True)
def fetch_ads(message):
    text = message.text
    data = fetch_divar_ads(text)
    for item in data["web_widgets"]["post_list"][1:11]:
        title = item["data"]["title"]
        top_description_text = item["data"]["top_description_text"]
        middle_description_text = item["data"]["middle_description_text"]
        bottom_description_text = item["data"]["bottom_description_text"]
        photo = item["data"]["image_url"][0]["src"]
        token = item["data"]["token"]
        description = f"{title}\n{top_description_text}\n{middle_description_text}\n{bottom_description_text}\nhttps://divar.ir/v/{token}"
        bot.send_photo(chat_id=message.chat.id,caption=description,photo=photo)
        


bot.infinity_polling()