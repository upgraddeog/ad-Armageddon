# Advertising Armageddon – Google Ads + GPT Streamlit Dashboard

This Streamlit app helps you manage and optimize Google Ads campaigns using GPT-4, Google Sheets, and Google Ads API.

## ✨ Features
- Google OAuth login + credential management
- Create and manage Google Ads campaigns, ad groups, and responsive ads
- Live ad preview before publishing
- Bulk ad variant generation using OpenAI GPT-4
- Google Sheets logging for campaign insights
- Onboarding wizard and GUI-based API credential entry

## 🧪 Local Development

1. Clone this repo
2. Run `pip install -r requirements.txt`
3. Create a `.env` file with your API keys or use the GUI to input and save them
4. Start with `streamlit run main.py`

## 🚀 Deployment (Streamlit Cloud Recommended)
- Upload files
- Use `.streamlit/secrets.toml` or the GUI input to enter credentials at runtime

## 📝 Logging
- All user actions are saved to `logs.txt` locally
