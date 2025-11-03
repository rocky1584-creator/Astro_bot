from flask import Flask, request
import telegram
import datetime
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "Astrology Bot is active 🌟"

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == '/start':
        bot.sendMessage(chat_id=chat_id, text="🌞 Welcome to AstroGuru! Type /daily to receive your astrology message.")
    elif text == '/daily':
        today = datetime.date.today().strftime('%A, %d %B %Y')
        message = f"✨ {today}\nYour stars suggest calmness and clarity today. Focus on inner peace and gratitude."
        bot.sendMessage(chat_id=chat_id, text=message)
    else:
        bot.sendMessage(chat_id=chat_id, text="Type /daily for your astrology update 🌙")

    return 'ok'

if __name__ == "__main__":
    app.run(port=5000)
