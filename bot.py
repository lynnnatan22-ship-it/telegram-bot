from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ================== CONFIG ==================
TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"
ADMIN_ID = 393655145  # <-- replace with YOUR Telegram user ID
CHANNEL_ID = "@cokfiko"
BOT_LINK = "https://t.me/CofikoBot"

# ================== MENUS ==================
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_ID)],
        [InlineKeyboardButton("🤖 Open Bot", url=BOT_LINK)],
        [InlineKeyboardButton("📤 Post (Admin)", callback_data="post")],
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")]
    ])

def back_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ])

# ================== START ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to COKFIKO Business Bot",
        reply_markup=main_menu()
    )

# ================== BUTTONS ==================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    # INFO PAGE
    if query.data == "info":
        await query.edit_message_text(
            "ℹ️ This is your business control bot.\nUse buttons below.",
            reply_markup=back_menu()
        )

    # BACK
    elif query.data == "back":
        await query.edit_message_text(
            "🏠 Main Menu",
            reply_markup=main_menu()
        )

    # ADMIN POST
    elif query.data == "post":
        if user_id != ADMIN_ID:
            await query.edit_message_text("❌ Not authorized")
            return

        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text="🔥 NEW UPDATE FROM COKFIKO SYSTEM"
        )

        await query.edit_message_text("✅ Posted to channel", reply_markup=main_menu())

# ================== COMMAND POST ==================
async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("❌ No permission")
        return

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="🔥 MANUAL POST FROM ADMIN"
    )

    await update.message.reply_text("✅ Posted to channel")

# ================== MAIN ==================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
