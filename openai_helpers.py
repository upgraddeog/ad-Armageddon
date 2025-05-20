import openai

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

def gpt_persona_brief(analytics_data, ad_data):
    prompt = (
        "Given this analytics and ad data, define the 1-2 most likely buyer personas, including their top pain points, motivations, and what content would most convert them:\n"
        f"Analytics Data: {analytics_data}\n"
        f"Ad Data: {ad_data}\n"
    )
    return gpt_response(prompt)

def gpt_pain_point_article(negative_keywords, low_conv_copy, product):
    prompt = (
        f"Write a content brief and intro for an article targeting customers hesitant to buy '{product}'. "
        f"Address their pain points (from these negative keywords: {', '.join(negative_keywords)}) "
        f"and improve on this low-performing copy: '{low_conv_copy}'."
    )
    return gpt_response(prompt)

def gpt_trending_content(trending_queries, site_niche):
    prompt = (
        f"Suggest 3 fresh content ideas (with draft headlines and summaries) for a {site_niche} website, targeting these trending search queries:\n"
        f"{', '.join(trending_queries)}"
    )
    return gpt_response(prompt)

def gpt_response(prompt):
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
    )
    return resp.choices[0].message['content']
