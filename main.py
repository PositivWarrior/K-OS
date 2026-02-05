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

    part = response.candidates[0].content.parts[0]
    function_responses = []

    if part.function_call:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("Function call result has no parts")

            resp_obj = function_call_result.parts[0].function_response
            if resp_obj is None:
                raise Exception("FunctionResponse is None")

            if resp_obj.response is None:
                raise Exception("FunctionResponse.response is None")

            function_responses.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {resp_obj.response}")

    elif part.text:
        print(f"Response:\n{part.text}")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(f"Response:\n {response.text}")

if __name__ == "__main__":
    main()
