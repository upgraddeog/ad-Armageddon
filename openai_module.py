import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_ad_variants(prompt, n_variants=3):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
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
            model="gpt-4",
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
