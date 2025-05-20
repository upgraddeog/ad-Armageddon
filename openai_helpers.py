import openai
import os

# Optional: Set API key here or rely on secrets.toml
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Blog / Content Generator ---
def gpt_content_ideas(keyword, ad_copy, persona, site_niche, competitors=None):
    prompt = (
        f"You are an expert SEO and CRO strategist for a {site_niche} website.\n"
        f"Generate 5 unique, conversion-focused blog post ideas (titles + 1-sentence summaries) "
        f"for the keyword: '{keyword}', using this ad copy as context: '{ad_copy}'."
    )
    if persona:
        prompt += f"\nTarget persona: {persona}."
    if competitors:
        prompt += f"\nMain competitors: {', '.join(competitors)}."
    prompt += "\nIdeas must be ultra-specific and have high potential to rank and convert."
    return gpt_response(prompt)

def gpt_competitor_gap(keyword, competitor_titles):
    prompt = (
        f"You are an SEO analyst. Given the following top-ranking titles for '{keyword}':\n"
        f"{chr(10).join('- ' + t for t in competitor_titles)}\n"
        f"Suggest unique angles, missing subtopics, or superior content opportunities to outrank them."
    )
    return gpt_response(prompt)

def gpt_faq_schema(topic):
    prompt = (
        f"Write a list of 5 highly relevant FAQ questions and answers for the topic: '{topic}'. "
        f"Then generate valid schema.org JSON-LD for these FAQs."
    )
    return gpt_response(prompt)

# --- Ad Copy & Insight Enhancers ---
def generate_ad_variants(base_ad):
    prompt = (
        f"Write 3 A/B test ad variants based on this ad:\n'{base_ad}'\n"
        f"Each version should test different tones, CTAs, or offers."
    )
    return gpt_response(prompt).split("\n\n")

def analyze_ad_creative(ad_text):
    prompt = (
        f"You're a performance marketer. Analyze this ad for tone, clarity, persuasiveness, and suggestions to improve CTR:\n\n{ad_text}"
    )
    return gpt_response(prompt)

def summarize_insights(insight_text):
    prompt = (
        "You're a digital strategist. Summarize the performance data and key trends from this campaign data:\n\n"
        f"{insight_text}"
    )
    return gpt_response(prompt)

def generate_tags_from_metrics(metrics_text):
    prompt = (
        "Generate 5 performance-based tags or labels based on this ad/campaign metric report:\n\n"
        f"{metrics_text}"
    )
    return gpt_response(prompt)

def budget_recommendation(metrics_text):
    prompt = (
        "Given this ad performance data, recommend one action for budget scaling (increase, hold, reduce) and why:\n\n"
        f"{metrics_text}"
    )
    return gpt_response(prompt)

# --- Persona & Simulation Tools ---
def generate_personas(analytics_data, ad_data):
    prompt = (
        f"Based on the following analytics and ad results, describe 2 likely audience personas including motivations, objections, and key content types:\n\n"
        f"Analytics:\n{analytics_data}\n\nAd Data:\n{ad_data}"
    )
    return gpt_response(prompt)

def simulate_competitors(niche):
    prompt = (
        f"Generate 3 fake but realistic ad examples that a top competitor in the '{niche}' industry might run.\n"
        "Include headlines and descriptions."
    )
    return gpt_response(prompt)

# --- Core Chat Completion Function ---
def gpt_response(prompt):
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
    )
    return resp.choices[0].message['content']
