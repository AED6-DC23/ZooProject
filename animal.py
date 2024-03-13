import telebot
from config import token
from telebot import types
from config import photo2, photo3, photo4, photo5, photo6, photo7, photo8

bot = telebot.TeleBot(token)
text1 = 'в этом боте я прошёл тест и узнал, что мое тотемное животное '
text2 = "твоё тотемное животное - "
text3 = 'Стать опекуном - участие в программе «Возьми животное под опеку» — это ваш личный вклад в дело сохранения биоразнообразия Земли и развитие нашего зоопарка.\n' \
        '\Основная задача Московского зоопарка с самого начала его существования это — сохранение биоразнообразия нашей планеты. Когда вы берете под опеку животное, вы помогаете нам в этом благородном деле.\n' \
        'Для подробной информации обратитесь к работнику'

def cot(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)

    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo2,
                   caption=f'{call.message.chat.username}{text2} кот!  '
                           f'\nКот, все кошачьи - наделяет владельца делать дела "украдкой", подкрадываться незаметно. Качества: любопытство,независимость, мягкость, ласка. Владелец такого тотема более живучий. \n{text3}',
                   reply_markup=markup)

def ric(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo3,
                   caption=f'{call.message.chat.username}{text2} рысь'
                           f'\nРысь - Рысь носительница тайн. Рысь свободно двигается во времени и пространстве, ей свойственна прозорливость и дальновидность, видит "нутро", распознает ложь и обман.\n{text3}',
                   reply_markup=markup)

def tiger(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo4,
                   caption=f'{call.message.chat.username}{text2} тигр!'
                           f'\nТигр - творец и разрушитель. Королевское достоинство, жестокость, сила, власть, мужество и ярость.\n{text3}',
                   reply_markup=markup)

def jaguar(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo5,
                   caption=f'{call.message.chat.username}{text2} ягуар! '
                           f'\nЯгуар - только сильный и могущественный шаман мог обладать тотемом ягуара. Мудрость, могущество, стремительность, великолепный следопыт.\n{text3}',
                   reply_markup=markup)

def barc(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo6,
                   caption=f'{call.message.chat.username}{text2} барс!  '
                           f'\nБарс - свирепость, ярость, агрессивность, безжалостность. Хороший "щит" и защитник от негатива.\n{text3}',
                   reply_markup=markup)

def leopard(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo7,
                   caption=f'{call.message.chat.username}{text2} леопард!  '
                           f'\nЛеопард - жестокость, свирепость, агрессивность, смелость. Символ храбрости, стремительности, активности. Сила этого тотема может быть как созидательной, так и разрушительной. \n{text3}',
                   reply_markup=markup)

def lev(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text1)
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo8,
                   caption=f'{call.message.chat.username}{text2} лев!  '
                           f'\nЛев - олицетворяет собой силу, великолепие, храбрость, стойкость, справедливость, закон, военную мощь. Также символизирует звериный образ жизни. Он — символ войны и является атрибутом богов войны.\n{text3}',
                   reply_markup=markup)
