from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"

CHANNEL_LINK = "https://t.me/cokfiko"
BOT_LINK = "https://t.me/CofikoBot"

# Bottom menu button (persistent)
menu_keyboard = ReplyKeyboardMarkup(
    [["🚀 Open Menu"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🤖 Bot", url=BOT_LINK)]
    ]

    await update.message.reply_text(
        "👋 Welcome!\nChoose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🤖 Bot", url=BOT_LINK)]
    ]

    await update.message.reply_text(
        "📌 Main Menu:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
