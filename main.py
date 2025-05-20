import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up page configuration
st.set_page_config(page_title="Advertising Armageddon", layout="wide")

# Sidebar navigation
st.sidebar.title("🔧 Navigation")
selection = st.sidebar.radio("Go to", ["Dashboard", "Campaign Manager", "Keyword Manager", "Insights", "Settings"])

# Main title
st.title("🚀 Advertising Armageddon")

# Content based on selection
if selection == "Dashboard":
    st.subheader("📊 Overview")
    st.write("Summary of your campaign performance and KPIs.")

elif selection == "Campaign Manager":
    st.subheader("🎯 Campaign Manager")
    st.write("Upload campaigns, generate A/B variants, manage targeting.")
    st.button("Generate A/B Variants")
    st.file_uploader("Upload Campaign CSV", type=["csv"])

elif selection == "Keyword Manager":
    st.subheader("🔑 Keyword Manager")
    st.write("GPT suggestions for keyword targeting and geo options.")
    st.text_input("Enter product/service description")
    st.button("Suggest Keywords")

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
