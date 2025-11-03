import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get your Telegram token and Render URL from environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")
APP_URL = os.getenv("RENDER_EXTERNAL_URL")  # Render sets this automatically

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌟 Hello! Your Astrology Bot is now live.")

@app.route("/")
def home():
    return "Astro Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    application.create_task(application.process_update(update))
    return "OK"

if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # Set webhook to Render URL
    if APP_URL:
        webhook_url = f"{APP_URL}/{TOKEN}"
        print("Setting webhook to:", webhook_url)
        application.bot.set_webhook(webhook_url)
    
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
