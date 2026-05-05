from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8715059765:AAFYlCPl-4IZ-_Vow2kbTDiVyWq6MMdsy-c"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working ✅")


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot running...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
