from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8712010632:AAHLvzvXKd4JhKaIeBJjAjgJXa791Dh3tUU"

async def javob(update: Update, context: ContextTypes.DEFAULT_TYPE):
    xabar = update.message.text.lower()

    if "salom" in xabar:
        await update.message.reply_text("Salom! 😊 Qalaysiz?")
    elif "yaxshi" in xabar:
        await update.message.reply_text("Doimo yaxshi bo‘ling! 😄")
    elif "isming nima" in xabar:
        await update.message.reply_text("Mening ismim UZB_ALISA_BOT 🤖")
    else:
        await update.message.reply_text(
            "Siz yozdingiz: " + update.message.text
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, javob))

print("UZB_ALISA_BOT ishga tushdi!")
app.run_polling()