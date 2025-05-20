import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_ad_variants(prompt, n_variants=3):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
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

def suggest_keywords(description):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a digital marketing expert specialized in keyword targeting."},
                {"role": "user", "content": f"Suggest 10 PPC keywords for this product or service: {description}"}
            ],
            temperature=0.5,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error suggesting keywords: {e}"

def summarize_insights(metrics_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a marketing analyst. Summarize campaign performance based on KPIs."},
                {"role": "user", "content": metrics_text}
            ],
            temperature=0.6,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error summarizing insights: {e}"

def analyze_ad_creative(ad_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert ad reviewer. Provide actionable feedback on this ad copy."},
                {"role": "user", "content": ad_text}
            ],
            temperature=0.6,
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error analyzing ad copy: {e}"

def generate_tags_from_metrics(metrics_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Read the following campaign metrics and output 3 tags (e.g., 'High Spend', 'Low CTR')."},
                {"role": "user", "content": metrics_text}
            ],
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error generating tags: {e}"

def budget_recommendation(metrics_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Based on the following metrics, recommend whether to increase, maintain, or decrease the ad budget."},
                {"role": "user", "content": metrics_text}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error making budget recommendation: {e}"
