import schedule
import time
import pytz
from datetime import datetime
import os
from main import send_email
from dotenv import load_dotenv

load_dotenv()
UG_TIMEZONE = pytz.timezone(os.getenv("TIMEZONE", "Africa/Kampala"))

def job():
    now = datetime.now(UG_TIMEZONE)
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Running email job...")
    send_email()

# Schedule jobs
schedule.every().day.at("07:00").do(job)
schedule.every().day.at("23:00").do(job)

print("Scheduler running...")

while True:
    schedule.run_pending()
    time.sleep(30)
