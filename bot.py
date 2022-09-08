import config
import telebot

from hh_parcing import parce_data
from handle_data import handle_vacancoes
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['check'])

def get_vacancies(message):
    raw_data = parce_data()
    data = handle_vacancoes(raw_data)
    for text in data[:5]:
        bot.send_message(message.chat.id, text)

if __name__ == '__main__':
     bot.infinity_polling()

