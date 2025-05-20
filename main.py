import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Example usage of environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Dummy route to your dashboard logic
def run_dashboard():
    st.set_page_config(page_title="Advertising Armageddon")
    st.title("Advertising Armageddon Dashboard")
    st.write("Welcome! This dashboard connects to Google Ads and Meta Ads.")
    st.write(f"Using OpenAI Key: {'✅ Loaded' if OPENAI_API_KEY else '❌ Not Found'}")

if __name__ == "__main__":
    run_dashboard()
