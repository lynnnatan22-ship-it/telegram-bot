from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# 🔑 TOKEN (BotFather)
TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"

# 📢 CHANNEL
CHANNEL_USERNAME = "@CofikoBot"
CHANNEL_LINK = "https://t.me/CofikoBot"

# 📊 STORE USERS
users = set()

# 🔍 CHECK IF USER IN CHANNEL
async def is_member(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# 🚀 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    users.add(user_id)

    joined = await is_member(context.bot, user_id)

    if not joined:
        keyboard = [
            [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
            [InlineKeyboardButton("🔄 I Joined", callback_data="check")]
        ]

        await update.message.reply_text(
            "🚨 You must join the channel first:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    keyboard = [
        [InlineKeyboardButton("📊 Crypto Signals", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 Contact", url="https://t.me/yourusername")]
    ]

    await update.message.reply_text(
        "👋 Welcome!\nChoose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# 📢 MANUAL POST
async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Sending update to all users...")

    for user in list(users):
        try:
            await context.bot.send_message(
                chat_id=user,
                text="🚀 New Crypto Signal Update!"
            )
        except:
            pass

# ⏰ AUTO MESSAGE LOOP
async def auto_post(app):
    while True:
        for user in list(users):
            try:
                await app.bot.send_message(
                    chat_id=user,
                    text="📊 Auto Crypto Update"
                )
            except:
                pass

        await asyncio.sleep(3600)

# 🔧 STARTUP
async def on_startup(app):
    asyncio.create_task(auto_post(app))

def main():
    app = Application.builder().token(TOKEN).post_init(on_startup).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()