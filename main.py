import os
import argparse
from dotenv import load_dotenv
from google import genai

def main():
    parser = argparse.ArgumentParser(description="K-OS: Agentic AI Enviorment")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI Agent")
    args = parser.parse_args()

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        print("GEMINI_API_KEY not found in .env file")
        exit(1)

    client = genai.Client(api_key=api_key)

    model_id = "gemini-2.5-flash"
    contents = args.user_prompt

    response = client.models.generate_content(
        model=model_id,
        contents=contents,
        )

    if response.usage_metadata is None:
        raise RuntimeError("API request failed: usage_metadata is missing")

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n {response.text}")

if __name__ == "__main__":
    main()
