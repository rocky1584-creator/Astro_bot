import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
APP_URL = os.getenv("RENDER_EXTERNAL_URL")

if not TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN not found in environment variables!")

app = Flask(__name__)

# Telegram command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌟 Hello! Your Astrology Bot is now live and running via Render.")

# Create bot app
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Webhook endpoint — Telegram sends updates here
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "OK", 200

@app.route("/")
def home():
    return "✅ Astrology Bot is running on Render.", 200

if __name__ == "__main__":
    # Set webhook URL for Telegram
    webhook_url = f"{APP_URL}/{TOKEN}"
    print(f"🚀 Setting webhook to: {webhook_url}")
    application.bot.set_webhook(url=webhook_url)

    # Run Flask app (Render exposes this webserver)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
