import telebot
from config import token
from telebot import types
from animal import lev, cot, tiger, jaguar, barc, ric, leopard

bot = telebot.TeleBot(token)

point = 0
lvl = 0

# кнопки перед началом викторины с возможностью возврата в главное меню
@bot.message_handler(commands=['quiz'])
def quiz(message):
    bot.send_message(message.chat.id, text="Эта викторина определит твоё тотемное животное^_^")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Главное меню')
    btn2 = types.KeyboardButton('🏆Начать викторину🏆')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "❗Главное меню❗ /  "
                                           "🏆Начать викторину🏆", reply_markup=markup)

# первый вопрос
def quest1(message):
    global point
    global lvl
    point = 0
    lvl = 0
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("Построить карьеру", callback_data='1')
    info_button2 = types.InlineKeyboardButton("Семья", callback_data='2')
    info_button3 = types.InlineKeyboardButton("Веселье с друзьями", callback_data='3')
    markup.add(info_button1, info_button2, info_button3)
    bot.send_message(message.chat.id, "Что тебе сейчас интереснее всего?", reply_markup=markup)
    quest2(message)

# второй вопрос
def quest2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("Улыбки близких", callback_data='4')
    info_button2 = types.InlineKeyboardButton("Деньги", callback_data='5')
    info_button3 = types.InlineKeyboardButton("Окружающий мир", callback_data='6')
    markup.add(info_button1, info_button2, info_button3)
    bot.send_message(message.chat.id, "Что тебя неизменно радует?", reply_markup=markup)
    quest3(message)

# третий вопрос
def quest3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("Море", callback_data='7')
    info_button2 = types.InlineKeyboardButton("Солнце", callback_data='8')
    info_button3 = types.InlineKeyboardButton("Закат", callback_data='9')
    markup.add(info_button1, info_button2, info_button3)
    bot.send_message(message.chat.id, "Что из перечисленного тебе больше по душе?", reply_markup=markup)

# подсчёт очков для определения тотемного животного
@bot.callback_query_handler(func=lambda call: True)
def callback2(call):
    global point
    global lvl
    if call.data == "1":
        point += 1
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="1ый вопрос \U00002705", reply_markup=None)
    if call.data == "2":
        point += 2
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="1ый вопрос \U00002705", reply_markup=None)
    if call.data == "3":
        point += 3
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="1ый вопрос \U00002705", reply_markup=None)
    if call.data == "4":
        point += 1
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="2ой вопрос \U00002705", reply_markup=None)
    if call.data == "5":
        point += 2
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="2ой вопрос \U00002705", reply_markup=None)
    if call.data == "6":
        point += 3
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="2ой вопрос \U00002705", reply_markup=None)
    if call.data == "7":
        point += 1
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3ий вопрос \U00002705", reply_markup=None)
    if call.data == "8":
        point += 2
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3ий вопрос \U00002705", reply_markup=None)
    if call.data == "9":
        point += 3
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3ий вопрос \U00002705", reply_markup=None)
    if lvl == 3:
        bot.send_message(call.message.chat.id, " Викторина заверешена!")
        if point == 3:
            cot(call)
        if point == 4:
            ric(call)
        if point == 5:
            tiger(call)
        if point == 6:
            jaguar(call)
        if point == 7:
            barc(call)
        if point == 8:
            leopard(call)
        if point == 9:
            lev(call)

    print(point)
