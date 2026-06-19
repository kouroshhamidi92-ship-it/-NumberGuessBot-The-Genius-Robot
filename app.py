from flask import Flask, jsonify
import threading
import os
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "🤖 ربات نابغه‌باز در حال اجراست!",
        "platform": os.getenv("PLATFORM", "telegram"),
        "version": "7.0.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

def run_bot():
    """اجرای ربات در یک ترد جداگانه"""
    import bot
    try:
        bot.main()
    except Exception as e:
        print(f"❌ خطا در اجرای ربات: {e}")
        sys.exit(1)

# اجرای ربات در ترد جداگانه (برای gunicorn)
bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread.start()
print("✅ ربات در ترد جداگانه شروع به کار کرد")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)