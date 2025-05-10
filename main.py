from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from config import BOT_TOKEN
from books import BOOKS_LIST

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  
    button = [[InlineKeyboardButton("Поздороваться", callback_data="print_books")]]
    await update.message.reply_text(  
        text=f"Привет, {update.message.from_user.first_name}!",
        reply_markup=InlineKeyboardMarkup(button) 
    )

async def print_books(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    text = (
        "Список прочитанных книг:\n\n"
        + "\n".join(BOOKS_LIST)
    )
    await query.message.reply_text(text=text)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(print_books))
app.run_polling()