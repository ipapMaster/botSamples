import json
import random
import requests
import lxml
from bs4 import BeautifulSoup as b
import telebot
from telebot import types

url = 'https://finewords.ru/cit/citaty-so-smyslom'


def parser(url):
    r = requests.get(url)  # get запрос с сайта
    # print(r.text)  # код страницы
    soup = b(r.text, 'lxml')  # создаем объект soup, передаем ему выкачанный текст, запускаем html.parser
    content = soup.find_all('div', class_='cit')
    return [c.text for c in content]
    # print(clear_content)


list_quotes = parser(url)
random.shuffle(list_quotes)

bot = telebot.TeleBot('5978307749:AAGj48uFMb6NyY2STYJcQxqAcMEs4O6Y_zk')


@bot.message_handler(commands=['start'])
def start(message):
    """создадим клавиатуру, которая будет использоваться как меню"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Гороскоп')
    item2 = types.KeyboardButton('Погода')
    item3 = types.KeyboardButton('Цитата дня')
    keyboard.add(item1, item2, item3)  # чтобы добавить кнопки
    bot.send_message(message.chat.id, 'Здравствуйте, выберите пункт меню.', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def bot_massage(message):
    if message.chat.type == 'private':
        if message.text == 'Гороскоп':
            keyboard = types.ReplyKeyboardMarkup(row_width=3)
            item1 = types.KeyboardButton('Овен')
            item2 = types.KeyboardButton('Телец')
            item3 = types.KeyboardButton('Близнецы')
            item4 = types.KeyboardButton('Рак')
            item5 = types.KeyboardButton('Лев')
            item6 = types.KeyboardButton('Дева')
            item7 = types.KeyboardButton('Весы')
            item8 = types.KeyboardButton('Скорпион')
            item9 = types.KeyboardButton('Стрелец')
            item10 = types.KeyboardButton('Козерог')
            item11 = types.KeyboardButton('Водолей')
            item12 = types.KeyboardButton('Рыбы')
            back = types.KeyboardButton('Назад')

            keyboard.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,
                         item12, back)  # чтобы добавить кнопки
            bot.send_message(message.chat.id, 'Выберите свой Знак Зодиака:', reply_markup=keyboard)
        elif message.text == 'Погода':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')

            keyboard.add(back)  # чтобы добавить кнопки
            bot.send_message(message.chat.id, 'Введите город:', reply_markup=keyboard)
            bot.register_next_step_handler(message, get_weather)

        elif message.text == 'Цитата дня':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')

            keyboard.add(back)  # чтобы добавить кнопки
            bot.send_message(message.chat.id, f'Ваша цитата сегодня: {list_quotes[0]}', reply_markup=keyboard)
            del list_quotes[0]

        elif message.text == 'Назад':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Гороскоп')
            item2 = types.KeyboardButton('Погода')
            item3 = types.KeyboardButton('Цитата дня')
            keyboard.add(item1, item2, item3)  # чтобы добавить кнопки
            bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=keyboard)

        elif message.text == 'Овен':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url1 = 'https://horo.mail.ru/prediction/aries/today/'
            r = requests.get(url1)
            soup = b(r.text, 'lxml')
            content_aries = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
            list_aries = [c.text for c in content_aries]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_aries[0]}', reply_markup=keyboard)

        elif message.text == 'Телец':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url2 = 'https://horo.mail.ru/prediction/taurus/today/'
            r = requests.get(url2)
            soup = b(r.text, 'lxml')
            content_taurus = soup.find_all('div',
                                           class_='article__item article__item_alignment_left article__item_html')
            list_taurus = [c.text for c in content_taurus]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_taurus[0]}', reply_markup=keyboard)

        elif message.text == 'Близнецы':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url3 = 'https://horo.mail.ru/prediction/gemini/today/'
            r = requests.get(url3)
            soup = b(r.text, 'lxml')
            content_gemini = soup.find_all('div',
                                           class_='article__item article__item_alignment_left article__item_html')
            list_gemini = [c.text for c in content_gemini]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_gemini[0]}', reply_markup=keyboard)

        elif message.text == 'Рак':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url4 = 'https://horo.mail.ru/prediction/cancer/today/'
            r = requests.get(url4)
            soup = b(r.text, 'lxml')
            content_cancer = soup.find_all('div',
                                           class_='article__item article__item_alignment_left article__item_html')
            list_cancer = [c.text for c in content_cancer]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_cancer[0]}', reply_markup=keyboard)

        elif message.text == 'Лев':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url5 = 'https://horo.mail.ru/prediction/leo/today/'
            r = requests.get(url5)
            soup = b(r.text, 'lxml')
            content_leo = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
            list_leo = [c.text for c in content_leo]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_leo[0]}', reply_markup=keyboard)

        elif message.text == 'Дева':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url6 = 'https://horo.mail.ru/prediction/virgo/today/'
            r = requests.get(url6)
            soup = b(r.text, 'lxml')
            content_virgo = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
            list_virgo = [c.text for c in content_virgo]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_virgo[0]}', reply_markup=keyboard)

        elif message.text == 'Весы':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url7 = 'https://horo.mail.ru/prediction/libra/today/'
            r = requests.get(url7)
            soup = b(r.text, 'lxml')
            content_libra = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
            list_libra = [c.text for c in content_libra]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_libra[0]}', reply_markup=keyboard)

        elif message.text == 'Скорпион':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url8 = 'https://horo.mail.ru/prediction/scorpio/today/'
            r = requests.get(url8)
            soup = b(r.text, 'lxml')
            content_scorpio = soup.find_all('div',
                                            class_='article__item article__item_alignment_left article__item_html')
            list_scorpio = [c.text for c in content_scorpio]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_scorpio[0]}', reply_markup=keyboard)

        elif message.text == 'Дева':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url9 = 'https://horo.mail.ru/prediction/sagittarius/today/'
            r = requests.get(url9)
            soup = b(r.text, 'lxml')
            content_sagittarius = soup.find_all('div',
                                                class_='article__item article__item_alignment_left article__item_html')
            list_sagittarius = [c.text for c in content_sagittarius]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_sagittarius[0]}',
                             reply_markup=keyboard)

        elif message.text == 'Дева':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url10 = 'https://horo.mail.ru/prediction/capricorn/today/'
            r = requests.get(url10)
            soup = b(r.text, 'lxml')
            content_capricorn = soup.find_all('div',
                                              class_='article__item article__item_alignment_left article__item_html')
            list_capricorn = [c.text for c in content_capricorn]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_capricorn[0]}', reply_markup=keyboard)

        elif message.text == 'Водолей':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url11 = 'https://horo.mail.ru/prediction/aquarius/today/'
            r = requests.get(url11)
            soup = b(r.text, 'lxml')
            content_aquarius = soup.find_all('div',
                                             class_='article__item article__item_alignment_left article__item_html')
            list_aquarius = [c.text for c in content_aquarius]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_aquarius[0]}', reply_markup=keyboard)

        elif message.text == 'Рыбы':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            keyboard.add(back)
            url12 = 'https://horo.mail.ru/prediction/pisces/today/'
            r = requests.get(url12)
            soup = b(r.text, 'lxml')
            content_pisces = soup.find_all('div',
                                           class_='article__item article__item_alignment_left article__item_html')
            list_pisces = [c.text for c in content_pisces]
            # print(list_aries)
            bot.send_message(message.chat.id, f'Ваш гороскоп на сегодня: \n {list_pisces[0]}', reply_markup=keyboard)


def get_weather(message):
    try:
        city = message.text
        key = 'fdaa3fcaf6fabd1b949b0025881f9855'
        result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric')
        weather = result.json()
        temp = weather['main']['temp']
        #       print(temp)
        temp1 = round(temp, 1)
        bot.send_message(message.from_user.id, f' Температура в городе {city} сейчас: {temp1} C градусов')
        # bot.send_message(message.from_user.id, f'Введите город')
    except Exception:
        bot.send_message(message.from_user.id, f'Нет такого {city}')
        bot.send_message(message.from_user.id, f'Введите город')
        bot.register_next_step_handler(message, get_weather)


bot.polling(none_stop=True)
