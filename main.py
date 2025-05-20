import streamlit as st
import streamlit as st
from openai_module import generate_ad_variants, suggest_keywords
import schedule
import time
import threading


st.set_page_config(page_title="Advertising Armageddon", layout="wide")

st.sidebar.title("🔧 Navigation")
selection = st.sidebar.radio("Go to", ["Dashboard", "Campaign Manager", "Keyword Manager", "Insights", "Settings"])

st.title("🚀 Advertising Armageddon")

if selection == "Dashboard":
    st.subheader("📊 Overview")
    st.write("Summary of your campaign performance and KPIs.")

elif selection == "Campaign Manager":
    st.subheader("🎯 Campaign Manager")

# Ad variant generation
st.markdown("**🧪 Generate A/B Variants**")
ad_prompt = st.text_area("Enter base ad description for GPT A/B generation")
if st.button("Generate A/B Variants"):
    if ad_prompt:
        variants = generate_ad_variants(ad_prompt)
        for idx, variant in enumerate(variants, 1):
            st.markdown(f"**Variant {idx}:**\n{variant}")
    else:
        st.warning("Please enter a base description to generate variants.")

# Ad creative feedback
st.markdown("---")
st.markdown("**🔍 Ad Creative Feedback**")
ad_feedback_input = st.text_area("Paste an existing ad for feedback")
if st.button("Get Feedback on Ad"):
    if ad_feedback_input:
        feedback = analyze_ad_creative(ad_feedback_input)
        st.text_area("GPT Feedback", value=feedback, height=200)
    else:
        st.warning("Please enter ad copy to get feedback.")

    ad_prompt = st.text_area("Enter base ad description for GPT A/B generation")
    if st.button("Generate A/B Variants"):
        if ad_prompt:
            variants = generate_ad_variants(ad_prompt)
            for idx, variant in enumerate(variants, 1):
                st.markdown(f"**Variant {idx}:**\n{variant}")
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

# KPI Trend Visualization (placeholder)
st.line_chart(data={"Example": [1, 2, 3, 4, 3, 5]})

# Insight summarizer
st.markdown("---")
st.markdown("**🧠 GPT Insight Summary**")
insight_input = st.text_area("Paste campaign KPIs or metrics")
if st.button("Summarize Insights"):
    if insight_input:
        summary = summarize_insights(insight_input)
        st.text_area("GPT Summary", value=summary, height=200)
    else:
        st.warning("Please paste metrics for insight summary.")

# Insight tags
st.markdown("**🏷️ Auto-Generated Tags**")
if st.button("Generate Tags"):
    if insight_input:
        tags = generate_tags_from_metrics(insight_input)
        st.text_area("Tags", value=tags, height=100)
    else:
        st.warning("Paste metrics above to generate tags.")

# Budget recommendation
st.markdown("**💸 Budget Recommendation**")
if st.button("Recommend Budget Action"):
    if insight_input:
        recommendation = budget_recommendation(insight_input)
        st.text_area("Budget Suggestion", value=recommendation, height=100)
    else:
        st.warning("Paste metrics above to analyze budget.")
    st.write("Visual trends with GPT-generated summaries and tags.")
    st.line_chart(data={"Example": [1, 2, 3, 4, 3, 5]})

elif selection == "Settings":
    st.subheader("⚙️ Integrations")

# Email SMTP configuration
st.markdown("### 📧 Email Summary Settings")
email_user = st.text_input("Sender Email Address (SMTP)")
email_pass = st.text_input("Email App Password (SMTP)", type="password")
email_to = st.text_input("Recipient Email Address")
email_subject = st.text_input("Email Subject", value="Your GPT Ad Performance Summary")
send_now = st.button("Send Email Summary Now")


# Scheduler configuration
st.markdown("### 🕒 Email Schedule")
enable_scheduler = st.checkbox("Enable Daily Email Summary (simulated with loop)")

# Store schedule status in session
if "email_scheduled" not in st.session_state:
    st.session_state.email_scheduled = False

def scheduled_task():
    from email_digest import send_gpt_email_summary
    if all([email_user, email_pass, email_to, insight_input]):
        result = send_gpt_email_summary(insight_input, email_user, email_pass, email_to, email_subject)
        print("Email sent via schedule:", result)

if enable_scheduler and not st.session_state.email_scheduled:
    schedule.clear()
    schedule.every().day.at("09:00").do(scheduled_task)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(60)

    threading.Thread(target=run_scheduler, daemon=True).start()
    st.session_state.email_scheduled = True
    st.success("✅ Daily email scheduling enabled (simulated loop active)")
elif not enable_scheduler:
    schedule.clear()
    st.session_state.email_scheduled = False


if send_now:
    if all([email_user, email_pass, email_to, insight_input]):
        from email_digest import send_gpt_email_summary
        result = send_gpt_email_summary(insight_input, email_user, email_pass, email_to, email_subject)
        st.success(result)
    else:
        st.warning("Please complete email fields and paste metrics in the Insights section.")


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
