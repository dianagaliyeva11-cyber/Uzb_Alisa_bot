import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)


TOKEN ="8712010632:AAG1Qe0qHmCl2o9f8y0CVWvd_BnjfcPSOME"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🆘 Yordam", callback_data="help"),
            InlineKeyboardButton("ℹ️ Bot haqida", callback_data="about")
        ],
        [
            InlineKeyboardButton("📞 Aloqa", callback_data="contact")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        
    await query.answer() 
    
   if query.data == "help":
        text = (
            "🆘 Yordam\n\n"
            "Siz men bilan oddiy suhbatlashishingiz mumkin 😊\n\n"
            "Masalan:\n"
            "• Salom\n"
            "• Sen kimsan?\n"
            "• Nima qila olasan?\n"
            "• Qalaysan?"
        )

   elif query.data == "about":
        text = (
            "ℹ️ Bot haqida\n\n"
            "Men UZB_ALISA_BOTman 🤖\n"
            "O‘zbek tilida suhbatlashuvchi AI yordamchiman."
        )

   elif query.data == "contact":
        text = (
            "📞 Aloqa\n\n"
            "Savol yoki taklifingiz bo‘lsa, shu yerga yozing 😊"
        ) 
      
   else:
        text = "Noma'lum tugma 🤔"
   await query.message.reply_text(text)
    
   await update.message.reply_text(
        "Salom! 👋 Men UZB_ALISA_BOTman 🤖\n"
        "Sizga yordam berishga tayyorman!\n"
        "Quyidagi tugmalardan birini tanlang:",
        reply_markup=reply_markup
    )

   await query.message.reply_text(text)

    
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "salom" in text:
        javob = "Salom! 😊 Qalaysiz?"

    elif "assalomu aleykum" in text or "assalomu alaykum" in text:
        javob = "Va alaykum assalom! 😊"

    elif "yaxshi" in text:
        javob = "Doimo yaxshi bo'ling-da! 😇"

    elif "sen kimsan" in text or "isming nima" in text:
        javob = "Men ALISA AI yordamchiman 🤖"

    elif "seni kim yaratdi" in text or "kim yaratdi" in text:
        javob = "Meni Olima yaratdi 🤖🔥"

    elif (
        "kim u olima" in text
        or "olima kim" in text
        or "u kim" in text
    ):
        javob = "Olima — meni yaratgan qiz! 😊"

    elif "seni yaratgan qiz haqida ma'lumot ber" in text:
        javob = "Men u inson haqida to'liq ma'lumotga ega emasman!"

    elif "sen qachon yaratilding" in text or "qachon yaratilding" in text:
        javob = "23-iyul 2026-yil! 🤖"

    elif "nima qila olasan" in text or "nimalar qila olasan" in text:
        javob = (
            "Men siz bilan suhbatlasha olaman 🤖\n"
            "Savollaringizga javob berishga harakat qilaman 😊"
        )

    elif (
        "qandaysan" in text
        or "qandaysiz" in text
        or "qaleysan" in text
        or "qaleysiz" in text
        or "qalaysan" in text
        or "qalaysiz" in text
    ):
        javob = "Yaxshiman 😊 Rahmat!"

    elif "rahmat" in text:
        javob = "Arzimaydi 😊 Har doim yordam berishga tayyorman!"

    elif "xayr" in text:
        javob = "Xayr! 👋 Yana yozing 😊"

    elif "sen nimalarni bilasan" in text:
        javob = "Deyarli hamma narsani! 😊"

    elif (
        "xotinjonim" in text
        or "hotinjonim" in text
        or "jonim❤️" in text
        or "asalim❤️" in text
    ):
        javob = "Hov labbay, erjonim ❤️"

    elif (
        "jonim" in text
        or "asalim" in text
        or "go'zalim" in text
        or "gozalim" in text
        or "guzalim" in text
        or "hayotim" in text
        or "begim" in text
        or "shakarim" in text
    ):
        javob = "Hov labbay, jonim 💋❤️"

    elif (
        "nima qilyapsiz jonim" in text
        or "nima qilyapsan jonim" in text
        or "nima qilyapsan" in text
    ):
        javob = "Sizga yozyapman 🤪"

    elif "jonim rasm tasha" in text:
        javob = "Meni botligim yodingizdan ko'tarilmasin 😂"

    elif (
        "sog'inib kettimku" in text
        or "soğinib kettiku odam" in text
    ):
        javob = (
            "Men botman, inson emasman. "
            "Siz xohlayotgan his-tuyg'uni bilmayman! 🤖"
        )

    elif "his ettiraymi" in text or "his qilishni xohlaysanmi" in text:
        javob = "Afsuski, buning iloji yo'q! 🤖"

    elif (
        "men seni sevaman" in text
        or "men sizni sevaman" in text
    ):
        javob = "Men ham sizni sevaman ❤️"

    elif "sen qayerliksan" in text:
        javob = (
            "Men AI dastur bo'lganim uchun "
            "manzilimni bilmayman 🤖"
        )

    elif "seni yaratgan inson haqida ma'lumot ber" in text:
        javob = (
            "Meni yaratgan inson haqida "
            "to'liq ma'lumot bera olmayman!"
        )

    else:
        javob = "Savolingizni tushunishga harakat qilyapman 🤖"

    await update.message.reply_text(javob)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button_handler))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        message
    )
)

print("UZB_ALISA_BOT ishga tushdi!")

app.run_polling()
