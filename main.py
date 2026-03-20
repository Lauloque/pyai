import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_functions import available_functions, call_function
from prompts import system_prompt


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

    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
                temperature=0,
            ),
        )

        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)

        usage_metadata = response.usage_metadata
        if usage_metadata is None:
            raise RuntimeError("Failed API request: 'usage_metadata' empty.")

        if args.verbose:
            print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
            print(f"Response tokens: {usage_metadata.candidates_token_count}")
        print("Response:")
        function_responses = list()
        if response.function_calls:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, args.verbose)
                if not function_call_result.parts:
                    raise Exception("function call result has no parts")
                if not function_call_result.parts[0].function_response:
                    raise Exception("function call result isn't a FunctionResponse")
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("function call has no valid response")
                function_responses.append(function_call_result.parts[0])
                if args.verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}"
                    )
            messages.append(types.Content(role="user", parts=function_responses))

        else:
            print(response.text)
            return
    else:
        print("Error: Maximum number of iterations reached without success.")
        sys.exit(1)


if __name__ == "__main__":
    main()
