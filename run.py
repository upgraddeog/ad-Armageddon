import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("✅ Environment loaded.")
    print("🚀 Launching Streamlit dashboard at http://localhost:8501 ...")
    subprocess.run(["streamlit", "run", "main.py"])

if __name__ == "__main__":
    main()
