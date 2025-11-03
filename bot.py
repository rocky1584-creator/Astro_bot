import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")  # or os.getenv("TOKEN") if you renamed
APP_URL = os.getenv("RENDER_EXTERNAL_URL")

app = Flask(__name__)

# --- Telegram bot logic ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌟 Hello! Your Astrology Bot is now live on Render!")

# Create Telegram Application
application = Application.builder().token(TOKEN).build()

# Add command handlers
application.add_handler(CommandHandler("start", start))

# Webhook route
@app.route("/" + TOKEN, methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"

@app.route("/")
def index():
    return "Astro Bot is running."

if __name__ == "__main__":
    # Set webhook (important for Render)
    if APP_URL and TOKEN:
        webhook_url = f"{APP_URL}/{TOKEN}"
        application.bot.set_webhook(url=webhook_url)
        print(f"Webhook set to {webhook_url}")
    else:
        print("Missing APP_URL or TOKEN, cannot set webhook.")
    
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
