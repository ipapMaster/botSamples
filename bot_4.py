import telebot
from telebot import types

# создаём бота (его объект)
bot = telebot.TeleBot('5978307749:AAGj48uFMb6NyY2STYJcQxqAcMEs4O6Y_zk')

name = ''
surname = ''
age = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Как Вас зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id,
                         'Я Вас не понял, напишите /start')


def get_name(message):
    global name
    if '/' in message.text:
        bot.send_message(message.from_user.id,
                         'Это не имя, а что-то похожее на команду')
    else:
        name = message.text
        bot.send_message(message.from_user.id,
                         f'Спасибо {name}, а как Ваша фамилия?')
        bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    if '/' in message.text:
        bot.send_message(message.from_user.id,
                         'Это не фамилия, а что-то похожее на команду')
    else:
        surname = message.text
        bot.send_message(message.from_user.id,
                         f'Спасибо {name} {surname}, а какой у Вас возраст?')
        bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    try:
        age = int(message.text)
    except ValueError:
        bot.send_message(message.from_user.id,
                         f'{name} {surname}, нужно ввести целое число!')
        bot.register_next_step_handler(message, get_age)
    else:
        question = f'Итак, Вы {name} {surname} и Вам {age} лет?'
        kb = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        kb.add(yes, no)
        bot.send_message(message.from_user.id, text=question, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(call):
    """
    :param call.data: это callback data, которую мы передали
    """
    if call.data == 'yes':
        # заканчиваем диалог
        bot.send_message(call.message.chat.id,
                         f'{name} {surname}, было приятно познакомиться')
    elif call.data == 'no':
        # начнём опрос сначала
        bot.send_message(call.message.chat.id,
                         'Тогда начнём всё сначала. Как Вас зовут?')
        bot.register_next_step_handler(call.message, get_name)


# бот работает непрерывно
bot.polling(none_stop=True, interval=0)
