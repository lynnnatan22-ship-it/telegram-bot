from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"

CHANNEL_USERNAME = "@cokfiko"
CHANNEL_LINK = "https://t.me/cokfiko"


# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🚀 Open Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 Contact", url="https://t.me/yourusername")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome!\n\nClick below to continue 👇",
        reply_markup=reply_markup
    )


# ---------------- POST BUTTON MESSAGE TO CHANNEL ----------------
async def post_to_channel(app):

    keyboard = [
        [InlineKeyboardButton("🚀 Open Bot", url="https://t.me/YOUR_BOT_USERNAME")],
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]
    ]

    await app.bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text="🔥 Welcome to COKFIKO Channel\n\nChoose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ---------------- MAIN ----------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # run once when bot starts
    async def on_startup(app):
        await post_to_channel(app)

    app.post_init(on_startup)

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
