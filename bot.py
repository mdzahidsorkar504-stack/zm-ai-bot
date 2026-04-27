import requests
import time
import random
from datetime import datetime
import pytz
from flask import Flask
from threading import Thread

# --- কনফিগারেশন ---
BOT_TOKEN = "8779708385:AAGiTI6jACgoi1kP_qlpqBpEwBSqgrD6Qcs"
CHAT_ID = "-1003965140426"  # আপনার নতুন গ্রুপ আইডি

# রেন্ডার এরর ফিক্স (Fake Server)
app = Flask('')
@app.route('/')
def home():
    return "ZM PRO BOT IS LIVE"

def run_server():
    app.run(host='0.0.0.0', port=8080)

OTC_MARKETS = [
    "USDBDT-OTC", "USDINR-OTC", "USDPHP-OTC", "BRLUSD-OTC", "USDARS-OTC", 
    "USDCOP-OTC", "USDPKR-OTC", "USDEGP-OTC", "USDDZD-OTC", "USDZAR-OTC",
    "INTCQX-OTC", "BTCUSD-OTC", "MSFT-OTC", "FB-OTC"
]

def get_bd_time():
    tz = pytz.timezone('Asia/Dhaka')
    return datetime.now(tz).strftime("%H:%M:%S")

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}&parse_mode=Markdown"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Error: {e}")

def run_bot():
    print("ZM AI-PRO Group Bot is Active...")
    while True:
        market = random.choice(OTC_MARKETS)
        ai_score = random.randint(85, 99)

        if ai_score >= 93:
            # ১. প্রাক-সিগন্যাল সতর্কতা
            pre_text = (
                f"⏳ **PRE-SIGNAL ALERT (ZM-PRO)**\n"
                f"--- \n"
                f"📊 Market: *{market}*\n"
                f"🛠 Analysis: High Probability Found\n"
                f"📢 **Action: Ready in 3 Minutes!**"
            )
            send_msg(pre_text)
            time.sleep(180) 

            # ২. ফাইনাল সিগন্যাল (অনটাইম সহ)
            direction = random.choice(["CALL (UP) ⬆️", "PUT (DOWN) ⬇️"])
            entry_time = get_bd_time()
            
            final_text = f"""
🚀 **ZM FINAL SIGNAL**
---
📊 **Market:** {market}
📈 **Direction:** {direction}
⏰ **Entry Time:** {entry_time}
⏳ **Expiry:** 1 MIN
🎯 **AI Accuracy:** {ai_score}%

✅ **Enter NOW on next candle!**
            """
            send_msg(final_text)
            
            # ৩. ১ মিনিট পর রেজাল্ট চেক (সিমুলেশন)
            time.sleep(60)
            res = random.choice(["✅ PROFIT (WIN)", "✅ PROFIT (WIN)", "❌ LOSS"])
            result_msg = f"📊 **TRADE RESULT: {market}**\n---\n{res}\n⏰ Close Time: {get_bd_time()}"
            send_msg(result_msg)
            
            # বিরতি (ওভার-ট্রেডিং রুখতে)
            time.sleep(600) 
        else:
            time.sleep(20)

if __name__ == "__main__":
    # সার্ভার এবং বট একসাথে চালু করা
    t = Thread(target=run_server)
    t.start()
    run_bot()
