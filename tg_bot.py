import telebot
from telebot import types

bot = telebot.TeleBot('7578284714:AAGwZUTCfm5zFEiysa8FDomDalVcmeLd998')

@bot.message_handler(commands=["id"])
def main(message):
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} {message.from_user.last_name} {message.from_user.username}')

@bot.message_handler(content_types=['photo'])
def get_poto(message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton( 'Как красиво!',url='https://google.com' )
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton( 'удалить фото',callback_data='delete' )
        btn3 = types.InlineKeyboardButton( 'изменить фото',callback_data='edit' )
        markup.row(btn2,btn3)
        bot.reply_to(message, 'какое красивое фото', reply_markup = markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
        if callback.data == 'delete':
                bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
        elif callback.data == 'edit':
                bot.edit_message_text('Edit text',callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
