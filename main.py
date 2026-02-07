import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="K-OS: Agentic AI Enviorment")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI Agent")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        types.Content(
            role="user", 
            parts=[types.Part(text=args.user_prompt)]
        )
    ]
    
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        print("GEMINI_API_KEY not found in .env file")
        exit(1)

    client = genai.Client(api_key=api_key)

    model_id = "gemini-2.5-flash"

    for i in range(20):
        response = client.models.generate_content(
            model=model_id,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
                temperature=0
            )
        )

        if response.usage_metadata is None:
            raise RuntimeError("API request failed: usage_metadata is missing")

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        part = response.candidates[0].content.parts[0] # TODO: Check if this is the best way to handle this

        if part.function_call:
            function_responses = []
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)
                function_responses.append(function_call_result.parts[0])

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            
            messages.append(types.Content(role="user", parts=function_responses))
            continue

        elif part.text:
            print(f"\nFinal response:\n{part.text}")
            return

    print(f"Error: Agent exceeded maximum iterations (20) without reaching a conclusion.")
    exit(1)

if __name__ == "__main__":
    main()
