import configparser
import telebot

config = configparser.ConfigParser()
config.read('config.ini')
bot = telebot.TeleBot(config['DEFAULT']['Token'])

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    bot.reply_to(message, message.text)
bot.polling(none_stop=True, interval=0)
