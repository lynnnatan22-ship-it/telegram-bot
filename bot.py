from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ---------------- YOUR SETTINGS ----------------
TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"

CHANNEL_ID = "@cokfiko"
CHANNEL_LINK = "https://t.me/cokfiko"
BOT_LINK = "https://t.me/CofikoBot"


# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📢 Open Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)]
    ]

    await update.message.reply_text(
        "👋 Welcome to COKFIKO System\n\nChoose an option below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ---------------- POST MESSAGE TO CHANNEL ----------------
async def send_channel_message(app):

    try:
        keyboard = [
            [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)],
            [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]
        ]

        await app.bot.send_message(
            chat_id=CHANNEL_ID,
            text="🔥 COKFIKO SYSTEM ONLINE\n\nTap below to continue 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        print("✅ Channel message sent")

    except Exception as e:
        print("❌ Error sending channel message:", e)


# ---------------- MAIN BOT ----------------
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    async def startup(app):
        await send_channel_message(app)

    app.post_init(startup)

    print("Bot is running...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
