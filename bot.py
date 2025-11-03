import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load token from environment variable
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN is not set in environment variables.")

# Create Flask app (Render uses this for health checks)
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Astrology Telegram Bot is running on Render."

# Define command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌟 Hello! Your Astrology Bot is live and ready to guide you.")

# Main block for polling
if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("🚀 Bot started successfully. Waiting for messages...")
    application.run_polling()        application.bot.set_webhook(url=webhook_url)
        print(f"Webhook set to {webhook_url}")
    else:
        print("Missing APP_URL or TOKEN, cannot set webhook.")
    
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
