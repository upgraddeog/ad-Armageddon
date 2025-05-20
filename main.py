
import streamlit as st
from openai_module import (
    generate_ad_variants, suggest_keywords, summarize_insights,
    analyze_ad_creative, generate_tags_from_metrics, budget_recommendation
)
import schedule
import threading
import time

st.set_page_config(page_title="Advertising Armageddon", layout="wide")

# --- Sidebar Branding ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/OpenAI_Logo.svg/512px-OpenAI_Logo.svg.png", width=160)
st.sidebar.title("🧭 Navigation")

selection = st.sidebar.radio("Choose Section", [
    "Dashboard", "Campaign Manager", "Keyword Manager",
    "Persona Generator", "Competitor Simulator",
    "Insights", "WordPress Content Hub",
    "Schema & SEO Tools", "Email & Slack Settings", "Settings"
])

st.title("🚀 Advertising Armageddon")

if selection == "Dashboard":
    st.subheader("📊 Overview")
    st.info("Campaign performance, highlights, and quick insights.")

elif selection == "Campaign Manager":
    st.subheader("🎯 Campaign Manager")
    st.markdown("**🧪 Generate A/B Variants**")
    prompt = st.text_area("Base ad copy")
    if st.button("Generate A/B Variants"):
        if prompt:
            variants = generate_ad_variants(prompt)
            for idx, v in enumerate(variants, 1):
                st.markdown(f"**Variant {idx}:** {v}")
            st.toast("✅ Variants created")
        else:
            st.warning("Please enter ad copy first.")

    st.markdown("---")
    st.markdown("**🔍 Ad Feedback**")
    ad = st.text_area("Paste ad text")
    if st.button("Get Feedback"):
        if ad:
            st.text_area("GPT Feedback", analyze_ad_creative(ad), height=200)
            st.toast("💬 Feedback generated")

elif selection == "Keyword Manager":
    st.subheader("🔑 Keyword Generator")
    desc = st.text_input("Describe your offer")
    if st.button("Suggest Keywords"):
        if desc:
            st.text_area("Keywords", suggest_keywords(desc), height=200)
            st.toast("🔎 Keywords generated")

elif selection == "Persona Generator":
    st.subheader("🧍 Persona Builder")
    analytics = st.text_area("Analytics Data")
    ads = st.text_area("Ad Performance Snippet")
    if st.button("Generate Personas"):
        if analytics and ads:
            from openai_helpers import generate_personas
            result = generate_personas(analytics, ads)
            st.text_area("Personas", result, height=250)
            st.toast("🙋 Personas generated")

elif selection == "Competitor Simulator":
    st.subheader("🆚 Competitor Ad Simulator")
    niche = st.text_input("Your Niche")
    if st.button("Simulate Competitors"):
        if niche:
            from openai_helpers import simulate_competitors
            result = simulate_competitors(niche)
            st.text_area("Simulated Ads", result, height=250)
            st.toast("📢 Simulated competitor ads")

elif selection == "Insights":
    st.subheader("📈 KPI Insight Generator")
    kpis = st.text_area("Paste Metrics")
    if st.button("Summarize Insights"):
        if kpis:
            st.text_area("Summary", summarize_insights(kpis), height=200)
            st.toast("🧠 Insights summarized")

    if st.button("Generate Tags"):
        if kpis:
            st.text_area("Tags", generate_tags_from_metrics(kpis))
            st.toast("🏷️ Tags ready")

    if st.button("Recommend Budget"):
        if kpis:
            st.text_area("Recommendation", budget_recommendation(kpis))
            st.toast("💸 Budget action ready")

elif selection == "WordPress Content Hub":
    st.subheader("📝 GPT WordPress Publisher")
    st.info("Use `dashboard.py` for the full experience.")

elif selection == "Schema & SEO Tools":
    st.subheader("🔖 FAQ & Schema Generator")
    topic = st.text_input("Topic")
    if st.button("Generate Schema"):
        from openai_helpers import gpt_faq_schema
        result = gpt_faq_schema(topic)
        st.code(result)
        st.toast("📚 FAQ + Schema generated")

elif selection == "Email & Slack Settings":
    st.subheader("📬 Slack & Email Digest Settings")
    st.markdown("Controls for digest sending, channels, schedule, and Slack alerts.")
    st.info("Configured via Streamlit secrets.toml")

elif selection == "Settings":
    st.subheader("⚙️ Global App Settings")
    st.markdown("API Keys, tokens, and credentials loaded from `secrets.toml`")

st.markdown("---")
st.caption("Part of the Advertising Armageddon suite © 2025")
