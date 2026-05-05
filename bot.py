from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"

# MAIN MENU
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url="https://t.me/cokfiko")],
        [InlineKeyboardButton("🤖 My Bot", url="https://t.me/CofikoBot")],
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to COKFIKO Menu",
        reply_markup=main_menu()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text(
            "📌 This is your menu bot.\nUse buttons below:",
            reply_markup=main_menu()
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
