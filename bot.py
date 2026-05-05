from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ---------------- SETTINGS ----------------
TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"
BOT_LINK = "https://t.me/CofikoBot"
CHANNEL_LINK = "https://t.me/cokfiko"


# ---------------- START MENU ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)],
        [InlineKeyboardButton("📢 Open Channel", url=CHANNEL_LINK)]
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\nChoose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ---------------- MAIN ----------------
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot running...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
