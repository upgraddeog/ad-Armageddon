📘 ADVERTISING ARMAGEDDON - GPT Ad Management Suite

This project is an all-in-one Streamlit dashboard to manage and optimize your digital ad campaigns across Google Ads, Meta (Facebook), WordPress, and more—powered by OpenAI's GPT-4.

---

🎯 FEATURES

✅ GPT Ad Copy Optimizer
✅ A/B Test Variant Generator
✅ Keyword Generator
✅ KPI Insight Summarizer
✅ Budget Action Recommender
✅ Auto Persona Generator
✅ Competitor Ad Simulator
✅ WordPress Content Publisher
✅ Schema + FAQ Generator
✅ SERP Rank Tracker
✅ Google Sheets Logging (optional)
✅ Slack Alerts (optional)
✅ Email Summary Digest (daily/weekly)

---

🧠 BUILT WITH

- Python (Streamlit)
- OpenAI API (GPT-4o)
- WordPress REST API
- Google Ads + Meta Ads (via tokens)
- SMTP (email_digest.py)
- Optional: Google Sheets, Slack, GA4

---

🔐 REQUIRED SECRETS (.env or /.streamlit/secrets.toml)

OPENAI_API_KEY=sk-...
WP_SITE=https://your-wordpress-site.com
WP_APP_USER=your-wp-username
WP_APP_PASSWORD=your-wp-password

# Optional:
SLACK_WEBHOOK=https://hooks.slack.com/...
SHEET_JSON={...}
GA4_PROPERTY_ID=...
EMAIL_USER=you@gmail.com
EMAIL_PASS=your-app-password

---

🚀 INSTALL & RUN LOCALLY

1. Clone/download this repo
2. Install Python packages:
   pip install -r requirements.txt
3. Launch the app:
   streamlit run main.py

---

🌐 STREAMLIT CLOUD DEPLOYMENT

1. Upload all files to a GitHub repo
2. Go to https://streamlit.io/cloud
3. Paste your repo URL and choose `main.py` as the app file
4. Add your secrets via Streamlit Cloud settings
5. Click Deploy 🚀

---

🧩 FOLDER STRUCTURE

- main.py → Navigation UI
- dashboard.py → WordPress + Content
- openai_module.py → GPT API logic
- email_digest.py → Email Summary Sender
- wp_api.py → WordPress Publish/Schedule
- requirements.txt → Dependencies
- README.txt → This file

---

📬 NEED HELP?
This project is part of the **Advertising Armageddon** suite. Built to empower marketers, not coders.

Contact: you@example.com (or replace with actual)

