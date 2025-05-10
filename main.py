from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  
    button = [[InlineKeyboardButton("Поздороваться", callback_data="say_hello")]]
    await update.message.reply_text(  
        text="Привет!",
        reply_markup=InlineKeyboardMarkup(button) 
    )

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(text=f"Привет, {query.from_user.first_name}!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(say_hello))
app.run_polling()