import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)
client = 0
r = 0

# кнопки оценки бота
@bot.message_handler(commands=['review'])
def review(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("1", callback_data='Единица')
    info_button2 = types.InlineKeyboardButton("2", callback_data='Двойка')
    info_button3 = types.InlineKeyboardButton("3", callback_data='Тройка')
    info_button4 = types.InlineKeyboardButton("4", callback_data='Четвёрка')
    info_button5 = types.InlineKeyboardButton("5", callback_data='Пятёрка')

    markup.add(info_button1, info_button2, info_button3, info_button4, info_button5)
    bot.send_message(message.chat.id, "Оцените бота по качеству: от 1 до 5", reply_markup=markup)

# подсчет клиентов
@bot.callback_query_handler(func=lambda call: True)
def callback3(call):
    global client
    global r
    if call.data == "Единица":
        client += 1
        r += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!☹️", reply_markup=None)
    if call.data == "Двойка":
        client += 1
        r += 2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!😟", reply_markup=None)
    if call.data == "Тройка":
        r += 3
        client += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!😑", reply_markup=None)
    if call.data == "Четвёрка":
        client += 1
        r += 4
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!🙂", reply_markup=None)
    if call.data == "Пятёрка":
        r += 5
        client += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!🥹", reply_markup=None)

# итог оценок
def ocenka(message):
    global r
    global client
    if client == 0:
        bot.send_message(message.chat.id, text="Оценок еще нет, но ты можешь стать первым:)", )
    else:
        rat = r // client
        bot.send_message(message.chat.id, text=f"Всего оценок  {client}"
                                               f"\nСредняя оценка бота- {rat}", )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn8 = types.KeyboardButton("Главное меню")
    markup.add(btn8)
