import telebot
from telebot import types

# создаём бота (его объект)
bot = telebot.TeleBot('5978307749:AAGj48uFMb6NyY2STYJcQxqAcMEs4O6Y_zk')


@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('start.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.from_user.id, '✋ Привет')


@bot.message_handler(commands=['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton(text='Сайт Яндекса',
                                          url='https://ya.ru')
    markup.add(btn_site)
    bot.send_message(message.chat.id,
                     'Нажми на кнопку и перейдёшь на Яндекс',
                     reply_markup=markup)


@bot.message_handler(commands=['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    swt_but = types.InlineKeyboardButton(text='Выбор',
                                         switch_inline_query='Telegram')
    markup.add(swt_but)
    bot.send_message(message.chat.id,
                     'Выберите чат',
                     reply_markup=markup)


@bot.message_handler(commands=['button'])
def button_message(message):
    """Вариант создания меню"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/start')
    btn2 = types.KeyboardButton('/switch')
    btn3 = types.KeyboardButton('/url')
    btn4 = types.KeyboardButton('Кнопка')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Ваш выбор', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Кнопка':
        print('dsfsdfsd')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Кнопка 2')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         'Что нужно?', reply_markup=markup)
    elif message.text == 'Кнопка 2':
        bot.send_message(message.chat.id,
                         'Спасибо за нажатие кнопки №2')
        bot.send_message(message.chat.id, '/button')
    else:
        markup = types.InlineKeyboardMarkup()
        swt_but = types.InlineKeyboardButton(text='Выбор сайта',
                                             url='https://mail.ru')
        markup.add(swt_but)
        bot.send_message(message.chat.id,
                         'Перейти на Mail.ru',
                         reply_markup=markup)


# бот работает непрерывно
bot.polling(none_stop=True, interval=0)
