import requests, json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8403872147:AAGiRREvZkm41r0mgXDUuxR2oByGoTkZt8U"

def start(update, context):
    update.message.reply_text("👋 Send me a link and I’ll try to bypass it!")

def bypass_link(update, context):
    url = update.message.text.strip()
    try:
        res = requests.post("https://freeseptemberapi.vercel.app/bypass", json={"url": url})
        data = res.text
        if "message" in data:
            update.message.reply_text("❌ Error: " + data)
        else:
            _j = json.loads(data)
            update.message.reply_text("✅ Bypassed URL:\n" + _j["url"])
    except Exception as e:
        update.message.reply_text("❌ Error: " + str(e))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, bypass_link))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
