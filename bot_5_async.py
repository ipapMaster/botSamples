import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler, filters

# логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

reply_keyboard = [['/address', '/site']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text('Я справочник', reply_markup=markup)

async def help_command(update, context):
    await update.message.reply_text('Я бот-справочник.')

async def address(update, context):
    await update.message.reply_text('ИПАП. СПб, Можайская, 2')

async def site(update, context):
    await update.message.reply_text('ИПАП. Сайт: https://ipap.ru')


# Обработчик сообщений
async def echo(update, context):
    """
    :param update: принимает сообщения
    :param context: доп. инфо о сообщении
    """
    await update.message.reply_text(update.message.text)


def main():
    app = Application.builder().token('5978307749:AAGj48uFMb6NyY2STYJcQxqAcMEs4O6Y_zk').build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    app.add_handler(text_handler)
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('site', site))
    app.add_handler(CommandHandler('address', address))
    app.run_polling()


if __name__ == '__main__':
    main()
