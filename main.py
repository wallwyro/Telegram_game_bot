from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config

main_keyboard = ReplyKeyboardMarkup(
    [["🎰 Tragamonedas"], ["📊 Menú"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Bienvenido a Casino Juegos 🎮\nSelecciona un juego con los botones de abajo:",
        reply_markup=main_keyboard
    )

async def tragamonedas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_game("tragamonedas")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Menú principal activo.", reply_markup=main_keyboard)

app = Application.builder().token(config.TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(MessageHandler(filters.Text("🎰 Tragamonedas"), tragamonedas))
app.add_handler(MessageHandler(filters.Text("📊 Menú"), menu))
app.run_polling()
