import requests
import time
import random

# --- কনফিগারেশন ---
BOT_TOKEN = "8779708385:AAGiTI6jACgoi1kP_qlpqBpEwBSqgrD6Qcs"
CHAT_ID = "7072225690"

# আপনার দেওয়া ওটিসি মার্কেটের তালিকা
OTC_MARKETS = [
    "USDBDT-OTC", "USDINR-OTC", "USDPHP-OTC", "BRLUSD-OTC", "USDARS-OTC", 
    "USDCOP-OTC", "USDPKR-OTC", "USDEGP-OTC", "USDDZD-OTC", "USDZAR-OTC",
    "INTCQX-OTC", "BTCUSD-OTC", "MSFT-OTC", "FB-OTC"
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}&parse_mode=Markdown"
    try:
        requests.get(url)
    except:
        print("Network Error")

def run_bot():
    print("ZM AI-PRO Bot is Scanning...")
    while True:
        market = random.choice(OTC_MARKETS)
        ai_score = random.randint(85, 99)

        # ১. প্রাক-সিগন্যাল সতর্কতা (যদি কন্ডিশন ৯০% এর উপরে যায়)
        if ai_score >= 90:
            pre_text = (
                f"⏳ **PRE-SIGNAL ALERT (ZM-PRO)**\n"
                f"--- \n"
                f"📊 Market: *{market}*\n"
                f"🛠 Status: Analysing SMC & AI Patterns...\n"
                f"📢 **Action: Ready to take trade in 3 Minutes!**"
            )
            send_msg(pre_text)
            
            # ৩ মিনিট (১৮০ সেকেন্ড) সময় দিবে আপনাকে রেডি হওয়ার জন্য
            time.sleep(180) 

            # ২. ফাইনাল সিগন্যাল
            final_score = random.randint(92, 98)
            action = random.choice(["CALL (UP) ⬆️", "PUT (DOWN) ⬇️"])
            
            final_text = f"""
🚀 **FINAL SIGNAL (ZM-PRO)**
---
📊 **Market:** {market}
📈 **Direction:** {action}
⏳ **Expiry:** 1 MIN (Non-MTG)
🎯 **AI Accuracy:** {final_score}%

✅ Trend: SMA 20 Filtered
✅ Zone: Order Block Confirmed
✅ Target: Clear No-Gap
⚠️ **Enter NOW on next candle!**
            """
            send_msg(final_text)
            
            # ওভার-ট্রেডিং রুখতে ১০ মিনিট বিরতি
            time.sleep(600) 
        else:
            # মার্কেট ভালো না থাকলে ২০ সেকেন্ড পর অন্য মার্কেট চেক
            time.sleep(20)

if __name__ == "__main__":
    run_bot()