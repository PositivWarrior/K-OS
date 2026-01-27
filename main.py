import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    print("GEMINI_API_KEY not found in .env file")
    exit(1)

client = genai.Client(api_key=api_key)

model_id = "gemini-2.5-flash"
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
    model=model_id,
    contents=contents,
)

if response.usage_metadata is None:
    raise RuntimeError("API request failed: usage_metadata is missing")

print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(f"Response:\n {response.text}")

def main():
    print("Hello from k-os!")


if __name__ == "__main__":
    main()
