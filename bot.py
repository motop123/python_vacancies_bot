import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['check'])

def get_vacancies(message):
    bot.send_message(message.chat.id, 'вакансии hh')



if __name__ == '__main__':
     bot.infinity_polling()

