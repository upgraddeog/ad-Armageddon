OpenAI + WordPress Content Dashboard

- Generate and publish GPT-powered content directly to WordPress.
- Use GPT for competitor gap, trending, FAQ/schema, persona, and pain-point content.
- REST actions: publish, optimize, schedule, rank—all from one app.

.env (or Streamlit secrets.toml) should include:
WP_SITE=https://your-wordpress-site.com
WP_APP_USER=your-wp-username
WP_APP_PASSWORD=your-app-password
OPENAI_API_KEY=sk-...

Install with:
pip install -r requirements.txt

Run with:
streamlit run dashboard.py
