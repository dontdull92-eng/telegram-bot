from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8557688323:AAGBhzA-HcP5hARNe_VyYOp9T_IdAcEp0vk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    name = user.first_name or "Deleted Account"

    text = f"""Hey ❄️ {name}!

Your inquiry/complain ticket was just forwarded by Mod - Henry .bdx,
navigate the rough web for further instruction
"""

    keyboard = [
        [InlineKeyboardButton("Click to navigate web", 
url="https://beldexen.pages.dev/")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
