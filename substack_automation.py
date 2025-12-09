import requests
import schedule
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

PERPLEXITY_API = "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"

BLOG_CONFIG = {
    "Monday": {
        "title": "Weekly Education Insights",
        "prompt": "Research education innovations from aeon.co, newyorker.com, foundingfuel.com. Write 500-word blog about latest ed-tech trends, style: veedaily19.substack.com"
    },
    "Tuesday": {
        "title": "AI Weekly Digest",
        "prompt": "Gather AI breakthroughs from aeon.co, project-syndicate.com, newyorker.com. Write 500-word accessible AI blog, style: veedaily19.substack.com"
    },
    "Wednesday": {
        "title": "Fintech Updates",
        "prompt": "Research fintech from foundingfuel.com, epw.in, theatlantic.com. Write 500-word practical fintech blog, style: veedaily19.substack.com"
    },
    "Thursday": {
        "title": "Resume Tips & Tricks",
        "prompt": "Best resume practices from newyorker.com, aeon.co. Write 500-word actionable resume guide with examples."
    },
    "Friday": {
        "title": "Free Resume Makers Review",
        "prompt": "Compile top free resume builders. Write 500-word review comparing tools with pros/cons."
    }
}

def get_blog_content(day):
    config = BLOG_CONFIG.get(day)
    if not config:
        return None
    
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "pplx-70b-online",
        "messages": [
            {
                "role": "user",
                "content": config["prompt"]
            }
        ]
    }
    
    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            json=payload,
            headers=headers,
            timeout=120
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error fetching content: {e}")
        return None

def post_to_substack(title, content):
    webhook_url = os.getenv("IFTTT_WEBHOOK_URL")
    
    if not webhook_url:
        print("⚠️  IFTTT_WEBHOOK_URL not set.")
        return False
    
    try:
        payload = {
            "value1": title,
            "value2": content,
            "value3": "https://mrkan.substack.com"
        }
        response = requests.post(webhook_url, json=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Error posting: {e}")
        return False

def scheduled_job():
    day = datetime.now().strftime("%A")
    print(f"\n📅 Running job for {day} at {datetime.now().strftime('%H:%M:%S')}")
    
    if day not in BLOG_CONFIG:
        print(f"⏭️  No blog scheduled for {day}")
        return
    
    print(f"🔄 Fetching from Perplexity...")
    content = get_blog_content(day)
    
    if content:
        title = BLOG_CONFIG[day]["title"]
        print(f"✨ Posting to Substack...")
        
        if post_to_substack(title, content):
            print(f"✅ Blog posted: {title}")
        else:
            print(f"⚠️  Posting failed")
    else:
        print("❌ Content generation failed")

schedule.every().monday.at("03:00").do(scheduled_job)
schedule.every().tuesday.at("03:00").do(scheduled_job)
schedule.every().wednesday.at("03:00").do(scheduled_job)
schedule.every().thursday.at("03:00").do(scheduled_job)
schedule.every().friday.at("03:00").do(scheduled_job)

print("🚀 Automation started. Running 24/7...")
print("⏰ Scheduled: Monday-Friday at 8:30 AM IST")

while True:
    schedule.run_pending()
    time.sleep(60)
