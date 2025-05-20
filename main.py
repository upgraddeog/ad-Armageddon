import streamlit as st
from dotenv import load_dotenv
import os
from openai_module import generate_ad_variants, suggest_keywords

load_dotenv()

st.set_page_config(page_title="Advertising Armageddon", layout="wide")

st.sidebar.title("🔧 Navigation")
selection = st.sidebar.radio("Go to", ["Dashboard", "Campaign Manager", "Keyword Manager", "Insights", "Settings"])

st.title("🚀 Advertising Armageddon")

if selection == "Dashboard":
    st.subheader("📊 Overview")
    st.write("Summary of your campaign performance and KPIs.")

elif selection == "Campaign Manager":
    st.subheader("🎯 Campaign Manager")
    ad_prompt = st.text_area("Enter base ad description for GPT A/B generation")
    if st.button("Generate A/B Variants"):
        if ad_prompt:
            variants = generate_ad_variants(ad_prompt)
            for idx, variant in enumerate(variants, 1):
                st.markdown(f"**Variant {idx}:**
{variant}")
        else:
            st.warning("Please enter a base description to generate variants.")

elif selection == "Keyword Manager":
    st.subheader("🔑 Keyword Manager")
    product_description = st.text_input("Enter product/service description")
    if st.button("Suggest Keywords"):
        if product_description:
            keywords = suggest_keywords(product_description)
            st.text_area("Suggested Keywords", value=keywords, height=200)
        else:
            st.warning("Please enter a description to get keyword suggestions.")

elif selection == "Insights":
    st.subheader("📈 Insights & Trends")
    st.write("Visual trends with GPT-generated summaries and tags.")
    st.line_chart(data={"Example": [1, 2, 3, 4, 3, 5]})

elif selection == "Settings":
    st.subheader("⚙️ Integrations")
    use_slack = st.checkbox("Enable Slack Integration")
    use_sheets = st.checkbox("Enable Google Sheets Integration")
    use_email = st.checkbox("Enable Email Reports")

    if use_slack:
        st.text_input("Slack Bot Token", type="password")

    if use_sheets:
        st.text_area("Paste Google Sheets Credentials JSON")

    if use_email:
        st.text_input("Recipient Email")

st.markdown("---")
st.caption("Advertising Armageddon © 2025")
