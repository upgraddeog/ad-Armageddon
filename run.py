import os
import subprocess
from dotenv import load_dotenv

def main():
    print("📦 Loading environment...")
    load_dotenv()

    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("❌ OPENAI_API_KEY not found in environment. Please check your .env or secrets.toml.")
        return

    print("✅ Environment loaded successfully.")
    print("🚀 Launching Advertising Armageddon dashboard at http://localhost:8501 ...")
    
    try:
        subprocess.run(["streamlit", "run", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Streamlit failed to launch: {e}")
    except Exception as ex:
        print(f"❌ Unexpected error: {ex}")

if __name__ == "__main__":
    main()
