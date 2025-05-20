# 🧠 Ad Optimization System

A no-code Streamlit dashboard to analyze, optimize, and track advertising campaigns using GPT and multi-channel data integrations.

## ✅ What You Can Do
- 💡 Generate GPT-powered campaign suggestions
- 🧪 Create A/B test ad copy variants
- 📊 View performance history by campaign, user, or tag
- 📚 Restore and compare insight versions
- 🔁 Export to PDF or Notion
- 🔗 Share permalinks and auto-resume sessions

## 🚀 One-Click Deploy (Streamlit Cloud)
1. Fork or clone this repo
2. Upload to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Set `streamlit_app/main.py` as the entry point
4. Add secrets like OpenAI key, Notion, Slack, etc.

## 📂 Folder Structure
ad-optimization-system/
├── streamlit_app/
│   ├── main.py (entry point)
│   ├── components/ (UI tabs)
│   └── utils/ (auth, GPT, API logic)
├── data_storage/ (state and logs)
├── sample_data/ (uploadable test CSVs)
├── .streamlit/config.toml
├── requirements.txt
└── README.md

## 📦 Requirements
Install locally with:
pip install -r requirements.txt

## 🛠 Secrets Required
OPENAI_API_KEY=...
SLACK_WEBHOOK_URL=...
GOOGLE_SERVICE_ACCOUNT_FILE=path/to/service_account.json
NOTION_API_KEY=...
NOTION_DATABASE_ID=...

## 🧪 Demo Credentials
Use test credentials or simulate campaign uploads with sample CSVs provided in `/sample_data`.

## 🙌 Contributors
Created with ❤️ using Streamlit, OpenAI, and Google APIs.
