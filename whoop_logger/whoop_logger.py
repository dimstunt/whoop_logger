import logging

from config import TELEGRAM_BOT_TOKEN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)
if not TELEGRAM_BOT_TOKEN:
    exit("Specify TELEGRAM_BOT_TOKEN at .env")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if effective_chat is None:
        logging.warning('effective_chat is None')
    else:
        keyboard = [[
            InlineKeyboardButton("Option 1", callback_data="option_1"),
            InlineKeyboardButton("Option 2", callback_data="option_2")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text="lets start",
            reply_markup=reply_markup
        )


async def new_event(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if effective_chat is None:
        logging.warning("eff chat is none")
    else:
        keyboard = [[
            InlineKeyboardButton("Option 1", callback_data="option_1"),
            InlineKeyboardButton("Option 2", callback_data="option_2")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text="choose option",
            reply_markup=reply_markup
        )


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        logging.warning("not a query")
    else:
        await query.answer()
        data = query.data
        if data == "option_1":
            text = "You selected option 1."
        elif data == "option_2":
            text = "You selected option 2."
        else:
            text = "Invalid option selected."
        if not query.message:
            exit()
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=text
        )


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    choose_event_handler = CommandHandler('new_event', new_event)
    application.add_handler(choose_event_handler)
    callback_handler = CallbackQueryHandler(button_callback)
    application.add_handler(callback_handler)
    application.run_polling()
