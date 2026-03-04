import telebot

TOKEN = "8665777863:AAFDoHUt2A8spONUDam12c8ZSUCAbfZx4VU"
CHANNEL_USERNAME = "@SOURYA_121_SYSTEM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"👋 Welcome!\n\n"
        f"👉 Please join our channel first:\n"
        f"https://t.me/{CHANNEL_USERNAME.replace('@','')}\n\n"
        f"After joining, send any message 😊"
    )

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    bot.send_message(
        message.chat.id,
        "👍 Thanks for your message!\n\n"
        "🔥 Join our channel for more updates:\n"
        "https://t.me/SOURYA_121_SYSTEM"
    )

print("Bot Started...")
bot.infinity_polling()
