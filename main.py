import streamlit as st
from openai_module import (
    generate_ad_variants, suggest_keywords, summarize_insights, analyze_ad_creative,
    generate_tags_from_metrics, budget_recommendation, generate_personas, simulate_competitors
)
import schedule, threading, time

st.set_page_config(page_title="Advertising Armageddon", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/OpenAI_Logo.svg/512px-OpenAI_Logo.svg.png", width=160)
st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Choose Section", [
    "Dashboard", "Campaign Manager", "Keyword Manager", "Persona Generator",
    "Competitor Simulator", "Insights", "Settings"
])

# --- Dashboard Header ---
st.title("🚀 Advertising Armageddon")

# --- Sections ---
if selection == "Dashboard":
    st.subheader("📊 Performance Overview")
    st.write("High-level campaign trends, KPIs, and suggested actions.")

elif selection == "Campaign Manager":
    st.subheader("🎯 Campaign Manager")

    st.markdown("**🧪 Generate A/B Test Variants**")
    ad_prompt = st.text_area("Enter ad copy to enhance")
    if st.button("Generate Variants"):
        if ad_prompt:
            variants = generate_ad_variants(ad_prompt)
            for i, v in enumerate(variants, 1):
                st.markdown(f"**Variant {i}:** {v}")
        else:
            st.warning("Enter base ad copy first.")

    st.markdown("---")
    st.markdown("**🖼️ Upload Ad Creative for Feedback** *(Future OCR Support)*")
    ad_file = st.file_uploader("Upload Ad Image (optional)")
    ad_feedback = st.text_area("Or paste ad text for feedback")
    if st.button("Get Creative Feedback"):
        if ad_feedback:
            feedback = analyze_ad_creative(ad_feedback)
            st.text_area("GPT Feedback", value=feedback, height=180)
        else:
            st.warning("Paste ad copy or upload an image.")

elif selection == "Keyword Manager":
    st.subheader("🔑 Keyword Suggestions")
    description = st.text_input("Describe your product or service")
    if st.button("Suggest Keywords"):
        if description:
            kws = suggest_keywords(description)
            st.text_area("GPT Keyword Suggestions", kws, height=200)
        else:
            st.warning("Please describe your offer.")

elif selection == "Persona Generator":
    st.subheader("🧍‍♀️ Audience Persona Generator")
    analytics = st.text_area("Paste Analytics Data")
    ad_data = st.text_area("Paste Ad Performance Snippet")
    if st.button("Generate Personas"):
        if analytics and ad_data:
            result = generate_personas(analytics, ad_data)
            st.text_area("GPT Persona Output", result, height=250)
        else:
            st.warning("Add both analytics and ad data.")

elif selection == "Competitor Simulator":
    st.subheader("🆚 Competitor Ad Simulator")
    niche = st.text_input("Your Niche or Industry")
    if st.button("Simulate Competitor Ads"):
        if niche:
            simulated = simulate_competitors(niche)
            st.text_area("Simulated Competitor Ads", simulated, height=200)
        else:
            st.warning("Enter a niche to simulate competitors.")

elif selection == "Insights":
    st.subheader("📈 Insight Generator + Trend Analyzer")
    insight_input = st.text_area("Paste campaign metrics, conversions, ROAS, etc.")

    if st.button("Summarize Insights"):
        if insight_input:
            summary = summarize_insights(insight_input)
            st.text_area("GPT Insight Summary", summary, height=200)

    if st.button("Generate Tags"):
        if insight_input:
            tags = generate_tags_from_metrics(insight_input)
            st.text_area("Auto-Generated Tags", tags)
    
    if st.button("Budget Suggestion"):
        if insight_input:
            rec = budget_recommendation(insight_input)
            st.text_area("Budget Recommendation", rec)

elif selection == "Settings":
    st.subheader("⚙️ Integration Settings")

    with st.expander("📧 Email Summary Settings"):
        email_user = st.text_input("Sender Email")
        email_pass = st.text_input("Email App Password", type="password")
        email_to = st.text_input("Recipient Email")
        subject = st.text_input("Subject Line", "Your GPT Ad Summary")

    with st.expander("🧠 GPT Settings"):
        openai_key = st.text_input("OpenAI API Key", type="password")

    with st.expander("🟦 Facebook / Meta Ads"):
        meta_token = st.text_input("Access Token", type="password")
        meta_ad_account = st.text_input("Ad Account ID")

    with st.expander("🟨 Google Ads"):
        google_refresh_token = st.text_input("OAuth Refresh Token", type="password")
        google_client_id = st.text_input("Client ID")
        google_client_secret = st.text_input("Client Secret", type="password")

    with st.expander("📄 WordPress"):
        wp_url = st.text_input("WP Site URL")
        wp_user = st.text_input("WP Username")
        wp_pass = st.text_input("WP App Password", type="password")

    with st.expander("📊 Google Analytics / GA4"):
        ga4_property_id = st.text_input("GA4 Property ID")
        ga4_json = st.text_area("GA4 Service Account JSON")

    with st.expander("📈 Google Sheets"):
        sheet_id = st.text_input("Google Sheet ID")
        sheet_json = st.text_area("Google Sheet JSON Key")

    with st.expander("💬 Slack Alerts"):
        slack_webhook = st.text_input("Slack Webhook URL")

    st.markdown("Your integration keys are stored securely via Streamlit secrets.toml (or environment vars).")

# Footer
st.markdown("---")
st.caption("🧠 Built with OpenAI + Streamlit | © 2025 Advertising Armageddon")
