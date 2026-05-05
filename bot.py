from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ---------------- SETTINGS ----------------
TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"

CHANNEL_LINK = "https://t.me/cokfiko"
BOT_LINK = "https://t.me/CofikoBot"


# ---------------- /START MENU ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)],
        [InlineKeyboardButton("📢 Open Channel", url=CHANNEL_LINK)]
    ]

    await update.message.reply_text(
        "👋 Welcome to Cofiko System\n\nChoose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ---------------- MAIN ----------------
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
