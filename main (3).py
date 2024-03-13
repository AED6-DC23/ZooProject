import telebot
from telebot import types
from config import token, chat_id
from ask import quiz, quest1, callback2, point
from ocenki import review, callback3, ocenka

bot = telebot.TeleBot(token)


# старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id,
                   photo='https://static.tildacdn.com/tild6433-3538-4335-b065-326532346236/MZoo-logo-ircle-mono.jpg',
                   caption=f'Добро пожаловать {message.from_user.first_name}! Предоставляю вашему внимаю нового бота Московского зоопарка. '
                           f'Тут вы сможете развлечься, пройдя викторину, благодаря которой узнаете ваше тотенмное животное. '
                           f'А также, сможете найти ссылки на сайты с информацией о животных на официальном сайте Московского зоопарка 🐯 ')
    menu(message)


# помощь
@bot.message_handler(commands=['help'])
def helper(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn8 = types.KeyboardButton("Главное меню")
    btn4 = types.KeyboardButton('Оценить бота')
    btn6 = types.KeyboardButton('Узнать оценки бота')
    btn5 = types.KeyboardButton('⚠Связаться с работником⚠')

    markup.add(btn8, btn4, btn5, btn6)
    bot.send_message(message.chat.id,
                     f'Вкладка "Помощь по навигации" предназначена для понятия, как устроен бот и как им пользоваться.\n'
                     f'В главном меню нажмите одну из кнопок.\n'
                     f'В энциклопедии находятся ссылки на прямые источники информации с официального сайта Московского зоопарка\n'
                     f'Во вкладке "Викторина" Вас ждёт увлекательный тест с набором баллов, в котором вы сможете узнать, каким тотемным животным вы являетесь:)\n'
                     f'А также сможете поделиться результатом со своими друзьями и пригласить их поучавствовать в чудо-викторине)'
                     f'\nПереходите в главное меню и развлекайтесь:)', reply_markup=markup)


# вызов помощи сотрудника
@bot.message_handler(commands=['sotrudnik'])
def sotrudnik(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn8 = types.KeyboardButton("Главное меню")
    markup.add(btn8)
    bot.send_message(message.chat.id, "Ожидайте, сотрудник ответит вам как можно скорее!!!", reply_markup=markup)
    bot.forward_message(chat_id, message.chat.id, message.message_id)


# вход в меню
@bot.message_handler(commands=['main_menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('↔Помощь по навигации↔')
    btn2 = types.KeyboardButton('📘Энциклопедия📘')
    btn3 = types.KeyboardButton('🏆Викторина🏆')

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, f"Выберите дальйшие действия: \n    ↔Помощь по навигации↔ "
                                           f"\n           📘Энциклопедия📘 "
                                           f"\n               🏆Викторина🏆", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    callback2(call)
    callback3(call)


# кнопки в энциклопедии
def animals1(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button9 = types.InlineKeyboardButton(text="Перейти на сайт", url="moscowzoo.ru")
    url_button10 = types.InlineKeyboardButton(text="Перейти в группу в телеграмме",
                                              url="https://t.me/Moscowzoo_official")
    keyboard.add(url_button9, url_button10)
    bot.send_message(message.chat.id, "Данный бот был разработан для дополнительного контента, но "
                                      "вы можете перейти в телеграм канал и сайт, где есть вся "
                                      "информация о животных", reply_markup=keyboard)


# все переходы кнопок и исключение
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Главное меню":
        bot.send_message(message.chat.id, text="Вы вернулись в Главное меню")
        menu(message)
    elif message.text == "↔Помощь по навигации↔":
        helper(message)
    elif message.text == "🏆Викторина🏆":
        quiz(message)
    elif message.text == "Оценить бота":
        review(message)
    elif message.text == "🏆Начать викторину🏆":
        quest1(message)
    elif message.text == "⚠Связаться с работником⚠":
        sotrudnik(message)
    elif message.text == "Узнать оценки бота":
        ocenka(message)
    elif message.text == "📘Энциклопедия📘":
        animals1(message)
    else:
        bot.send_message(message.chat.id, text="Управление ботом совершается исключительно кнопками", )


print(point)

bot.polling(none_stop=True)
