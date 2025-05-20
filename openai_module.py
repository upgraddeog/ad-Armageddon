import openai
import os

# Set up OpenAI API key (prefer environment or .streamlit/secrets.toml)
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai

# --- A/B Variant Generator ---
def generate_ad_variants(prompt, n_variants=3):
    """Generates multiple ad copy variants using GPT."""
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert ad copywriter."},
                {"role": "user", "content": f"Write {n_variants} ad copy variants for: {prompt}"}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return [choice.message.content.strip() for choice in response.choices]
    except Exception as e:
        return [f"❌ Error generating ad variants: {e}"]

# --- Keyword Suggestion ---
def suggest_keywords(description):
    """Suggests 10 relevant PPC keywords for a product or service."""
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a PPC strategist specialized in keyword targeting."},
                {"role": "user", "content": f"Suggest 10 PPC keywords for this product/service: {description}"}
            ],
            temperature=0.5,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error suggesting keywords: {e}"

# --- Insight Summary ---
def summarize_insights(metrics_text):
    """Summarizes KPIs and trends from ad campaign metrics."""
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a campaign analyst. Summarize performance KPIs."},
                {"role": "user", "content": metrics_text}
            ],
            temperature=0.6,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error summarizing insights: {e}"

# --- Ad Creative Feedback ---
def analyze_ad_creative(ad_text):
    """Provides GPT-generated feedback to improve an ad's effectiveness."""
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a creative strategist reviewing ad copy."},
                {"role": "user", "content": ad_text}
            ],
            temperature=0.6,
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error analyzing ad copy: {e}"

# --- Insight Tags ---
def generate_tags_from_metrics(metrics_text):
    """Suggests short tags or labels from performance reports."""
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Based on these metrics, generate 3 short tags (e.g. 'High Spend')."},
                {"role": "user", "content": metrics_text}
            ],
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error generating tags: {e}"

# --- Budget Adjustment ---
def budget_recommendation(metrics_text):
    """Recommends whether to increase, maintain, or lower the budget based on metrics."""
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Advise whether to increase, maintain, or reduce ad spend."},
                {"role": "user", "content": metrics_text}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error making budget recommendation: {e}"
