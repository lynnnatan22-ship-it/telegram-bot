from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = "8715059765:AAG5Vx5FaDcL2933qUR6VmXu2xLmOtfGb-k"
ADMIN_ID = 393655145
CHANNEL_ID = "@cokfiko"
BOT_LINK = "https://t.me/CofikoBot"

# ---------- MENU ----------
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_ID)],
        [InlineKeyboardButton("🤖 Bot", url=BOT_LINK)],
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")]
    ])

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Webhook Bot is running",
        reply_markup=main_menu()
    )

# ---------- CALLBACK ----------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "info":
        await q.edit_message_text(
            "ℹ️ Stable webhook mode active.",
            reply_markup=main_menu()
        )

# ---------- MAIN ----------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    # IMPORTANT: webhook mode (fixes conflict forever)
    port = int(os.environ.get("PORT", 8080))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"https://YOUR-RAILWAY-URL/{TOKEN}"
    )

if __name__ == "__main__":
    main()
