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


# ---------------- CHANNEL POST (SAFE ONLY) ----------------
async def post_to_channel(app):

    try:
        keyboard = [
            [InlineKeyboardButton("🚀 Open Bot", url=BOT_LINK)],
            [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]
        ]

        await app.bot.send_message(
            chat_id=CHANNEL_ID,
            text="🔥 COKFIKO SYSTEM ONLINE\n\nTap below to continue 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        print("✅ Channel post sent")

    except Exception as e:
        print("❌ Channel post failed:", e)


# ---------------- MAIN ----------------
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # SIMPLE SAFE STARTUP (NO JOBQUEUE, NO POST_INIT)
    async def startup():
        await post_to_channel(app)

    # run AFTER bot starts safely
    import asyncio
    asyncio.get_event_loop().create_task(startup())

    print("Bot is running...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
