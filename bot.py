import telebot
from decouple import config
from keyboards import inline_keyboard as in_key

bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hello my friend!', reply_markup=in_key)

bot.polling(none_stop=True)