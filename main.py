import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from analiza import analiza_companie

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Trimite un simbol bursier, ex: NVDA")

async def handle_symbol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    simbol = update.message.text.strip().upper()
    rezultat = analiza_companie(simbol)
    await update.message.reply_text(rezultat)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_symbol))
    app.run_polling()

if __name__ == "__main__":
    main()
