import streamlit as st
import wp_api
import openai_helpers as ai
import datetime

# --- Page Config ---
st.set_page_config(page_title="AI + WordPress Content Hub", layout="wide")

# --- Header & Intro ---
st.title("🚀 AI-Powered WordPress Content Dashboard")
st.markdown("""
Welcome to your unified content automation suite. Use GPT to:
- Generate ultra-specific blog ideas
- Analyze competitors
- Optimize and publish to WordPress
- Track performance — all in one place!
""")

# --- Sidebar with Help ---
st.sidebar.header("🔧 Settings")
st.sidebar.markdown("""
Add your API keys in `.env` or via Streamlit Cloud Secrets:
- `OPENAI_API_KEY`
- `WP_SITE`, `WP_APP_USER`, `WP_APP_PASSWORD`
""")
st.sidebar.info("Built by OpenAI + WordPress Enthusiasts ✨")

# --- Content Ideas ---
st.header("🔎 GPT-Powered Content Ideas")
site_niche = st.text_input("Your Website Niche", "Legal Tech")
keyword = st.text_input("Primary Keyword", "AI for law firms")
ad_copy = st.text_area("Top Performing Ad Copy", "Discover how AI transforms law firm efficiency…")
persona = st.text_input("Target Persona", "Small law firm owner")

if st.button("Generate Post Ideas"):
    with st.spinner("Thinking up gold..."):
        ideas = ai.gpt_content_ideas(keyword, ad_copy, persona, site_niche)
        st.markdown(ideas)

# --- Competitor Gap Analysis ---
st.header("💡 Competitor Gap Analysis")
comp_titles = st.text_area("Paste Top 3 Competitor Titles", "")
if st.button("Analyze Gaps"):
    with st.spinner("Analyzing SERP landscape..."):
        result = ai.gpt_competitor_gap(keyword, comp_titles.split("\n"))
        st.markdown(result)

# --- Post Management ---
st.header("📋 Publish / Schedule / Optimize")
title = st.text_input("Draft Title", "")
content = st.text_area("Draft Content", "")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Publish Now"):
        out = wp_api.publish_post(title, content, optimize=True)
        st.success(f"✅ Published: Post ID {out['post_id']}")
with col2:
    if st.button("Schedule for Tomorrow"):
        dt = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 09:00:00')
        out = wp_api.schedule_post(title, content, dt)
        st.success(f"📅 Scheduled: Post ID {out['post_id']} at 9:00 AM")
with col3:
    post_id_opt = st.text_input("Post ID to Optimize", "")
    if st.button("Optimize"):
        if post_id_opt:
            out = wp_api.optimize_post(int(post_id_opt))
            st.success(f"🔧 Optimized: Post ID {out['post_id']}")

# --- SERP Tracking ---
st.header("📈 Track SERP Rank")
serp_id = st.text_input("Post ID to Track Rank", "")
serp_rank = st.number_input("SERP Rank", min_value=1, max_value=100, value=1)
if st.button("Save SERP Rank"):
    out = wp_api.save_serp(int(serp_id), int(serp_rank))
    st.success(f"💾 Saved rank {serp_rank} for post {serp_id}")

# --- Trending Content Generator ---
st.header("🔥 Trending + Pain-point Content Automation")
trending_queries = st.text_area("Trending Queries", "AI law software, virtual paralegal, chatbots for law")
if st.button("Trending Content Ideas"):
    st.markdown(ai.gpt_trending_content(trending_queries.split(","), site_niche))

neg_kws = st.text_area("Negative Keywords", "expensive, unreliable, hard to use")
low_copy = st.text_area("Low-Performing Ad/Email Copy", "Switch to AI software today! (0.2% conversion)")
product = st.text_input("Your Product", "Legal AI Suite")
if st.button("Pain-Point Article Brief"):
    st.markdown(ai.gpt_pain_point_article(neg_kws.split(","), low_copy, product))

# --- Auto FAQ Schema ---
st.header("🔖 Auto FAQ + Schema Generator")
faq_topic = st.text_input("Topic for FAQ", keyword)
if st.button("Generate FAQ + Schema"):
    st.code(ai.gpt_faq_schema(faq_topic))

# --- Footer ---
st.markdown("---")
st.caption("This dashboard is part of the Advertising Armageddon AI Suite.")
