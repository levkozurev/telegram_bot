import telebot
from telebot import types

bot = telebot.TeleBot('7578284714:AAGwZUTCfm5zFEiysa8FDomDalVcmeLd998')

@bot.message_handler(commands=["id"])
def main(message):
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} {message.from_user.last_name} {message.from_user.username}')

@bot.message_handler(content_types=['photo'])
def get_poto(message):
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton( 'Что мне сказать?',url='https://google.com' ) )
        bot.reply_to(message, 'какое красивое фото', reply_markup = markup)
bot.polling(none_stop=True)