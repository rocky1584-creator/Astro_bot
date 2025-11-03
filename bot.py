import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")

# --- Telegram Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌞 Welcome to AstroGuru! Type /daily to receive your astrology message.")

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import date
    today = date.today().strftime('%A, %d %B %Y')
    msg = f"✨ {today}\nYour stars suggest calmness and clarity today. Focus on inner peace and gratitude."
    await update.message.reply_text(msg)

# Create the Telegram bot application
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("daily", daily))

# --- Flask Route for Telegram Webhook ---
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    application.update_queue.put_nowait(update)
    return "ok"

@app.route('/')
def index():
    return "Astrology Bot is active 🌟"

if __name__ == "__main__":
    # Start Flask app (Render will run this)
    app.run(port=5000)
