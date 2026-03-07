import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parser = argparse.ArgumentParser(
        description="Simple chatbot to... chat with... Original!"
    )
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="enable verbose output"
    )
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    print(f"User prompt: {args.user_prompt}") if args.verbose else None

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("Geminig API key not found.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    usage_metadata = response.usage_metadata
    if usage_metadata is None:
        raise RuntimeError("Failed API request: 'usage_metadata' empty.")

    if args.verbose:
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
