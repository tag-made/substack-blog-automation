# Substack Blog Automation

🤖 Fully automated Substack blog publishing using Perplexity AI + PythonAnywhere (runs 24/7)

## Features
- ✅ Zero manual input required
- ✅ Auto-generates blog posts using Perplexity Pro API
- ✅ Publishes to Substack daily at 8:30 AM IST
- ✅ Runs 24/7 on free PythonAnywhere account
- ✅ 5 different blog topics rotating Mon-Fri

## Setup Instructions (PythonAnywhere - Option A)

### Step 1: Clone Repository
```bash
git clone https://github.com/tag-made/substack-blog-automation.git
cd substack-blog-automation
```

### Step 2: Create PythonAnywhere Account
1. Go to: https://www.pythonanywhere.com
2. Sign up for free account
3. Confirm email

### Step 3: Upload Files to PythonAnywhere
1. In PythonAnywhere, go to "Files"
2. Upload `substack_automation.py`
3. Upload `requirements.txt`

### Step 4: Create `.env` File (Keep Secret!)
Create file with these credentials:
```
PERPLEXITY_API=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
SUBSTACK_EMAIL=your_email@gmail.com
SUBSTACK_PASSWORD=your_password
IFTTT_WEBHOOK_URL=https://maker.ifttt.com/trigger/substack_post/with/key/YOUR_KEY
```

### Step 5: Set Up IFTTT (Free)
1. Go to: https://ifttt.com
2. Create Applet:
   - If: Webhook ("substack_post")
   - Then: Send email with values
3. Copy webhook URL to .env

### Step 6: Install Dependencies
In PythonAnywhere Console:
```bash
pip install -r requirements.txt
```

### Step 7: Schedule Task
1. Go to "Web" tab in PythonAnywhere
2. Create "Scheduled Task"
3. Command: `python /home/username/substack_automation.py`
4. Time: Daily at 03:00 UTC (8:30 AM IST)
5. Enable task

## Blog Configuration

Edit `substack_automation.py` to customize:
- **Monday:** Education insights
- **Tuesday:** AI news
- **Wednesday:** Fintech updates  
- **Thursday:** Resume tips
- **Friday:** Free resume makers

## How It Works
1. Scheduler triggers at 8:30 AM IST daily
2. Script identifies day of week
3. Fetches content from Perplexity API
4. Sends to IFTTT webhook
5. IFTTT forwards to Substack
6. Blog auto-published ✅

## Files
- `substack_automation.py` - Main automation script
- `requirements.txt` - Python dependencies
- `.env` - Configuration (create yourself)

## Troubleshooting

**Script not running?**
- Check PythonAnywhere task is enabled
- Verify `.env` file in correct location
- Check API key is valid

**Blog not publishing?**
- Verify IFTTT webhook URL
- Check Substack credentials
- See PythonAnywhere logs for errors

## Support
For issues, check PythonAnywhere logs:
1. Go to Web tab
2. Scroll to "Scheduled Tasks"
3. Click task name to view output

---

**Status:** ✅ Ready to Deploy  
**Cost:** Free (PythonAnywhere Free + IFTTT Free)  
**Next:** Deploy on PythonAnywhere
