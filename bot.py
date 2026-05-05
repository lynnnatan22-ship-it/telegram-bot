from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"

CHANNEL_ID = "@cokfiko"
CHANNEL_LINK = "https://t.me/cokfiko"
BOT_LINK = "https://t.me/YOUR_BOT_USERNAME"


# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🚀 Open Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)]
    ]

    await update.message.reply_text(
        "👋 Welcome to COKFIKO System\n\nChoose below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ---------------- CHANNEL POST ----------------
async def send_channel_post(app):

    try:
        keyboard = [
            [InlineKeyboardButton("🚀 Open Bot", url=BOT_LINK)],
            [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]
        ]

        await app.bot.send_message(
            chat_id=CHANNEL_ID,
            text="🔥 COKFIKO SYSTEM ONLINE\n\nTap below 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        print("✅ Channel post sent")

    except Exception as e:
        print("❌ Error:", e)


# ---------------- MAIN ----------------
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    async def startup(app):
        await send_channel_post(app)

    app.post_init(startup)

    print("Bot is running...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
