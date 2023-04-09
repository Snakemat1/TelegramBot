import telebot
import webbrowser

from telebot import types

bot = telebot.TeleBot('6039517736:AAEs1vKM8klUlxGI2tNRvPc1AIx9-OhrnX0')
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://vk.com/cursedl0ve')
command = "/site, /lessons /help"
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Что я умею')
    markup.add(btn1)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == 'Что я умею':
        bot.send_message(message.chat.id, f'Вот мои команды: {command}')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,f'Вот мои команды:{command}, по остальным вопросам писать разработчику')






@bot.message_handler(commands=['lessons'])
def main(message):

    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Третье задание", url='https://www.youtube.com/watch?v=VvQ7GLMHcKA')
    btn2 = types.InlineKeyboardButton('Восьмое задание', url='https://www.youtube.com/watch?v=tLW_4euEnrk')
    btn3 = types.InlineKeyboardButton('Девятое задание', url='https://www.youtube.com/watch?v=SOt9bksT_bE')
    markup.row(btn1,btn2,btn3)
    btn4 = types.InlineKeyboardButton('Десятое задание', url='https://www.youtube.com/watch?v=aXPyeRRjr9c')
    btn5 = types.InlineKeyboardButton('Четырнадцатое задание', url='https://www.youtube.com/watch?v=BqXL7ntn5AQ')
    markup.row(btn4,btn5)
    bot.send_message(message.chat.id,'Вот разбор каждого задания: ', reply_markup=markup)




@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

#polling
bot.polling(none_stop=True)

