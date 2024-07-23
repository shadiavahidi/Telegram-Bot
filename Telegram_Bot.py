import logging

from telegram import Update

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7441896151:AAFugnWk0N7fhfzcgYMOw2zuWMsjhaJFJKI"

from pytz import timezone

tehran = timezone('Asia/Tehran')

logging.basicConfig(format='%(asctime)s – %(name)s – %(levelname)s – %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! من ربات تلگرام هستم.')


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN, use_context=True)


dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()

updater.idle()

if __name__ == '__main__':
    main()
