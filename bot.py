from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"
ADMIN_ID = 393655145  # replace with YOUR Telegram user ID

CHANNEL = "https://t.me/cokfiko"
BOT = "https://t.me/CofikoBot"

# ---------- MAIN MENU ----------
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url=CHANNEL)],
        [InlineKeyboardButton("🤖 Bot", url=BOT)],
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
        [InlineKeyboardButton("🔐 Admin", callback_data="admin")]
    ])

# ---------- BACK BUTTON ----------
def back_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ])

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to COKFIKO SYSTEM",
        reply_markup=main_menu()
    )

# ---------- CALLBACK HANDLER ----------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "info":
        await query.edit_message_text(
            "ℹ️ This is your advanced menu bot.\nBuilt for navigation.",
            reply_markup=back_menu()
        )

    elif query.data == "admin":
        if user_id == ADMIN_ID:
            await query.edit_message_text(
                "🔐 Admin Panel\n\nYou can extend this later (posts, stats, etc).",
                reply_markup=back_menu()
            )
        else:
            await query.edit_message_text(
                "❌ Access denied",
                reply_markup=main_menu()
            )

    elif query.data == "back":
        await query.edit_message_text(
            "🏠 Main Menu",
            reply_markup=main_menu()
        )

# ---------- MAIN ----------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
