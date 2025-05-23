import time
import requests
import random
import string
from datetime import datetime
from colorama import Fore, Style, init
init()

WEBHOOK = input("[💬] Enter your Webhook URL: ")

def log(msg, status="info"):
    prefix = {
        "info": f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL}",
        "success": f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}",
        "error": f"{Fore.RED}[ERROR]{Style.RESET_ALL}",
        "rate": f"{Fore.YELLOW}[RATELIMIT]{Style.RESET_ALL}"
    }.get(status, "")
    print(f"{prefix} {msg} {Fore.LIGHTBLACK_EX}- BY KHALID{Style.RESET_ALL}")

def send_webhook(username):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    embed = {
        "title": "🌟 Available Discord Username Found!",
        "color": 0x00FFC8,
        "fields": [
            {"name": "👤 Username", "value": f"`@{username}`", "inline": True},
            {"name": "📅 Found At", "value": now, "inline": True}
        ],
        "footer": {"text": "🔥 Tool by KHALID | Sniper Engine v1.0"},
        "timestamp": datetime.utcnow().isoformat()
    }
    try:
        requests.post(WEBHOOK, json={"embeds": [embed]})
    except:
        log("Webhook sending failed.", "error")

def gen_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

def check_username(username):
    try:
        r = requests.post(
            "https://discord.com/api/v9/unique-username/username-attempt-unauthed",
            json={"username": username}
        )
        if r.status_code == 200:
            if not r.json().get("taken", True):
                log(f"@{username} is AVAILABLE ✅", "success")
                send_webhook(username)
                with open("available.txt", "a", encoding="utf-8") as f:
                    f.write(f"{username} - Found by KHALID\n")
            else:
                log(f"@{username} is taken ❌", "error")
        elif r.status_code == 429:
            log("Rate limit detected. Cooling off...", "rate")
            time.sleep(10)
    except Exception as e:
        log(f"Error: {e}", "error")

def start_checker():
    log("🔥 Starting username sniping powered by KHALID...\n", "info")
    while True:
        username = gen_username()
        check_username(username)
        time.sleep(1)

if __name__ == "__main__":
    start_checker()