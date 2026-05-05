from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import asyncio

TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"
CHANNEL_USERNAME = "@cokfiko"
CHANNEL_LINK = "https://t.me/cokfiko"


# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # bottom menu buttons (persistent)
    keyboard = [
        ["🚀 Open Menu", "📢 Join Channel"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # main message + inline buttons
    inline = [
        [InlineKeyboardButton("🔥 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ Verify Access", callback_data="verify")]
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "To use this bot, join our channel first 👇",
        reply_markup=InlineKeyboardMarkup(inline)
    )

    await update.message.reply_text(
        "Use the buttons below 👇",
        reply_markup=reply_markup
    )


# ---------------- VERIFY ----------------
async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("⏳ Checking membership...")

    await asyncio.sleep(2)

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text("✅ Access granted! Welcome 🔥")
        else:
            keyboard = [
                [InlineKeyboardButton("🔥 Join Channel", url=CHANNEL_LINK)],
                [InlineKeyboardButton("🔄 Try Again", callback_data="verify")]
            ]

            await query.edit_message_text(
                "❌ You must join the channel first!",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    except:
        await query.edit_message_text("⚠️ Error checking access.")


# ---------------- BOTTOM BUTTONS ----------------
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚀 Open Menu":
        await update.message.reply_text(
            "🔥 Main Menu\n\n"
            "👉 Use the buttons above to navigate."
        )

    elif text == "📢 Join Channel":
        await update.message.reply_text(f"Join here 👉 {CHANNEL_LINK}")


# ---------------- MAIN ----------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
