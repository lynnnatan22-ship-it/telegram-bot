import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"

CHANNEL_ID = "@cokfiko"
CHANNEL_LINK = "https://t.me/cokfiko"
BOT_LINK = "https://t.me/YOUR_BOT_USERNAME"

# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🚀 Open Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)]
    ]

    await update.message.reply_text(
        "👋 Welcome to COKFIKO System\n\nChoose below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ---------------- SAFE CHANNEL POST ----------------
async def post_to_channel(app, retries=3):

    for attempt in range(retries):
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

            print("✅ Channel post successful")
            return

        except Exception as e:
            print(f"⚠️ Attempt {attempt+1} failed:", e)
            await asyncio.sleep(3)

    print("❌ All attempts failed")

# ---------------- STARTUP HANDLER ----------------
async def on_startup(app):
    await post_to_channel(app)

# ---------------- MAIN ----------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # guaranteed startup execution
    app.post_init(on_startup)

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
