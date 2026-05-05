from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8715059765:AAErHPw_S8C7JfyGvimnUcStmE9qPzi3V_Y"
CHANNEL_USERNAME = "@cokfiko"  # your channel

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Join Channel 🔥", url="https://t.me/cokfiko")],
        [InlineKeyboardButton("✅ Verify", callback_data="verify")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚀 Welcome!\n\n"
        "To use this bot, you must join our channel first 👇",
        reply_markup=reply_markup
    )

# VERIFY BUTTON
async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text("✅ Access granted! You can now use the bot.")
        else:
            await query.answer("❌ You must join the channel first!", show_alert=True)

    except:
        await query.answer("⚠️ Error checking membership. Try again.", show_alert=True)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
