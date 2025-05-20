import streamlit as st
import wp_api
import openai_helpers as ai
import datetime

# --- Page Config ---
st.set_page_config(page_title="Content Hub", layout="wide")

# --- Sidebar Logo ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/OpenAI_Logo.svg/512px-OpenAI_Logo.svg.png", width=150)
st.sidebar.title("🧭 WordPress Content")

# --- Header ---
st.title("📝 GPT-Powered WordPress Content Dashboard")
st.caption("Built with OpenAI + WordPress | Part of Advertising Armageddon")

# --- SECTION 1: Content Idea Generator ---
st.header("🔎 Generate GPT Content Ideas")
site_niche = st.text_input("🧭 Website Niche", "Legal Tech")
keyword = st.text_input("🔑 Primary Keyword", "AI for law firms")
ad_copy = st.text_area("📢 Top Performing Ad Copy", "Discover how AI transforms law firm efficiency…")
persona = st.text_input("👤 Target Persona", "Small law firm owner")

if st.button("💡 Generate Post Ideas"):
    with st.spinner("GPT is thinking..."):
        ideas = ai.gpt_content_ideas(keyword, ad_copy, persona, site_niche)
        st.markdown(ideas)

# --- SECTION 2: Competitor Gap Analysis ---
st.header("🥊 Competitor Gap Analysis")
comp_titles = st.text_area("🔍 Paste Top 3 Competitor Titles (1 per line)")
if st.button("Analyze Competitive Gaps"):
    with st.spinner("Analyzing SERP landscape..."):
        result = ai.gpt_competitor_gap(keyword, comp_titles.split("\n"))
        st.markdown(result)

# --- SECTION 3: Content Publishing Tools ---
st.header("📤 Publish / Schedule / Optimize Post")
title = st.text_input("📝 Draft Title")
content = st.text_area("📄 Draft Content", height=200)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🚀 Publish Now"):
        out = wp_api.publish_post(title, content, optimize=True)
        st.success(f"✅ Published: Post ID {out['post_id']}")
with col2:
    if st.button("📆 Schedule for Tomorrow"):
        dt = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 09:00:00')
        out = wp_api.schedule_post(title, content, dt)
        st.success(f"📅 Scheduled: Post ID {out['post_id']}")
with col3:
    post_id_opt = st.text_input("Post ID to Optimize")
    if st.button("🔧 Optimize"):
        if post_id_opt:
            out = wp_api.optimize_post(int(post_id_opt))
            st.success(f"🔍 Optimized: Post ID {out['post_id']}")

# --- SECTION 4: SERP Tracking ---
st.header("📈 SERP Rank Tracker")
serp_id = st.text_input("Post ID to Track")
serp_rank = st.number_input("Current SERP Rank", min_value=1, max_value=100, value=1)
if st.button("💾 Save SERP Rank"):
    out = wp_api.save_serp(int(serp_id), int(serp_rank))
    st.success(f"📊 Rank {serp_rank} saved for post {serp_id}")

# --- SECTION 5: Trending Content Generator ---
st.header("🔥 Trending + Pain-point Content")
trending_queries = st.text_area("🔍 Trending Queries (comma separated)", "AI law software, virtual paralegal")
if st.button("⚡ Generate Trending Content Ideas"):
    st.markdown(ai.gpt_trending_content(trending_queries.split(","), site_niche))

neg_kws = st.text_area("⚠️ Negative Keywords", "expensive, unreliable")
low_copy = st.text_area("🧊 Low-Performing Copy", "Switch to AI software today! (0.2% conversion)")
product = st.text_input("🛠️ Product Name", "Legal AI Suite")
if st.button("🩹 Generate Pain-Point Article Brief"):
    st.markdown(ai.gpt_pain_point_article(neg_kws.split(","), low_copy, product))

# --- SECTION 6: FAQ Schema Generator ---
st.header("🔖 Auto FAQ + Schema")
faq_topic = st.text_input("❓ FAQ Topic", keyword)
if st.button("📋 Generate FAQ + Schema"):
    st.code(ai.gpt_faq_schema(faq_topic))

# --- Footer ---
st.markdown("---")
st.caption("This module is part of the full cross-platform GPT optimization suite.")
