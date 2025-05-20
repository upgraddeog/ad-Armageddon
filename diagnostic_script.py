
# Diagnostic Script for Advertising Armageddon Streamlit App

import os
import importlib.util
import sys

REQUIRED_PACKAGES = [
    'streamlit',
    'pandas',
    'matplotlib',
    'plotly',
    'openai',
    'fpdf',
    'googleapiclient.discovery',
    'google.oauth2.credentials',
    'google_auth_oauthlib.flow',
    'requests',
    'dotenv',
    'slack_sdk',
    'gspread',
]

MISSING_PACKAGES = []

print("\nChecking required Python packages:")
for package in REQUIRED_PACKAGES:
    try:
        if '.' in package:
            importlib.import_module(package.split('.')[0])
        else:
            importlib.import_module(package)
        print(f"✓ {package}")
    except ImportError:
        print(f"✗ {package} (Missing)")
        MISSING_PACKAGES.append(package)

if MISSING_PACKAGES:
    print("\nPlease install missing packages with:")
    print("pip install " + ' '.join(set(pkg.split('.')[0] for pkg in MISSING_PACKAGES)))

print("\nChecking environment variables:")
REQUIRED_ENV_VARS = ['OPENAI_API_KEY', 'SLACK_BOT_TOKEN', 'GOOGLE_CLIENT_ID', 'GOOGLE_CLIENT_SECRET']

for var in REQUIRED_ENV_VARS:
    if os.getenv(var):
        print(f"✓ {var}")
    else:
        print(f"✗ {var} (Missing or not loaded)")

print("\nIf using a .env file, ensure it's loaded with python-dotenv or Streamlit secrets.")
