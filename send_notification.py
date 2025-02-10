import requests
import json
import os
from datetime import datetime
import pytz

# OneSignal API credentials (retrieved from GitHub Secrets)
ONESIGNAL_APP_ID = os.getenv("ONESIGNAL_APP_ID")
ONESIGNAL_API_KEY = os.getenv("ONESIGNAL_API_KEY")
GITHUB_UPDATE_URL = os.getenv("WEBPAGE_URL")  # URL to update.json

print(f"Using OneSignal App ID: {ONESIGNAL_APP_ID}")


# Timezone settings
utc = pytz.utc
est = pytz.timezone("America/New_York")

# Fetch the latest update from GitHub Pages
try:
    response = requests.get(GITHUB_UPDATE_URL)
    response.raise_for_status()
    update_data = response.json()
    latest_status = update_data.get("status", "New update available!")
    latest_timestamp_utc = update_data.get("timestamp", "")

    # Convert UTC to Eastern Time if the timestamp is in UTC format
    try:
        utc_time = datetime.strptime(latest_timestamp_utc, "%Y-%m-%d %H:%M UTC")
        est_time = utc_time.replace(tzinfo=utc).astimezone(est)
        latest_timestamp = est_time.strftime("%Y-%m-%d %I:%M %p ET")
    except ValueError:
        latest_timestamp = latest_timestamp_utc  # Use as-is if not UTC format

except Exception as e:
    print("Error fetching update file:", e)
    latest_status = "New update available!"
    latest_timestamp = ""

# Send a push notification via OneSignal API
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {ONESIGNAL_API_KEY}"
}

data = {
    "app_id": ONESIGNAL_APP_ID,
    "included_segments": ["All"],
    "headings": {"en": "Surgery Update"},
    "contents": {"en": f"{latest_status} (Updated: {latest_timestamp})"},
    "url": GITHUB_UPDATE_URL
}

response = requests.post("https://onesignal.com/api/v1/notifications", headers=headers, json=data)

if response.status_code == 200:
    print("Notification sent successfully!")
else:
    print("Failed to send notification:", response.json())
