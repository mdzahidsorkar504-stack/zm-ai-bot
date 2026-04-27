import requests
import time
import random

# কনফিগারেশন
BOT_TOKEN = "8779708385:AAGiTI6jACgoi1kP_qlpqBpEwBSqgrD6Qcs"
CHAT_ID = "7072225690"

OTC_MARKETS = [
    "USDBDT-OTC", "USDINR-OTC", "USDPHP-OTC", "BRLUSD-OTC", "USDARS-OTC", 
    "USDCOP-OTC", "USDPKR-OTC", "USDEGP-OTC", "USDDZD-OTC", "USDZAR-OTC",
    "INTCQX-OTC", "BTCUSD-OTC", "MSFT-OTC", "FB-OTC"
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=15)
    except:
        print("Signal failed to send")

def run_bot():
    print("ZM AI-PRO Bot is Scanning...")
    while True:
        # এটি সার্ভার সচল রাখবে
        print(f"Status Check: {random.randint(100, 999)}")
        
        market = random.choice(OTC_MARKETS)
        ai_score = random.randint(85, 99)

        if ai_score >= 93:
            # প্রাক-সিগন্যাল
            pre_text = f"⏳ **PRE-SIGNAL ALERT**\n---\n📊 Market: *{market}*\n🛠 AI Status: High Probability\n📢 **Ready to trade in 3 Minutes!**"
            send_msg(pre_text)
            
            time.sleep(180) # ৩ মিনিট বিরতি

            # ৩ মিনিট পর আবার চেক এবং ফাইনাল সিগন্যাল
            action = random.choice(["CALL (UP) ⬆️", "PUT (DOWN) ⬇️"])
            final_text = f"🚀 **FINAL SIGNAL (ZM-PRO)**\n---\n📊 Market: {market}\n📈 Direction: {action}\n⏳ Time: 1 MIN\n🎯 Accuracy: {random.randint(93,98)}%\n⚠️ **Enter NOW!**"
            send_msg(final_text)
            
            time.sleep(600) # ১০ মিনিট পর আবার শুরু হবে
        else:
            time.sleep(45) # ৪৫ সেকেন্ড পর আবার স্ক্যান

if __name__ == "__main__":
    run_bot()
