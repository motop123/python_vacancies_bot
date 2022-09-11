import config
import telebot
from telebot import types # для указание типов

from hh_parcing import parce_data
from handle_data import handle_vacancies
bot = telebot.TeleBot(config.token)

#----------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Вакансии")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Нужны свежие вакансии? Кликай!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def click_send_button(message):
    if(message.text == "👋 Вакансии"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="{0.first_name}, удачи в твоих поисках!".format(message.from_user), reply_markup=markup)
        raw_data = parce_data()
        data = handle_vacancies(raw_data)
        for text in data[:5]:
            bot.send_message(message.chat.id, text)


#----------------------------------------------------------------------------
if __name__ == '__main__':
     bot.infinity_polling()

