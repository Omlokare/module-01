"""A beginner AI study assistant. Run with: python study_buddy.py"""

import os

from openai import OpenAI


MODEL = "gpt-4o-mini"


def get_ai_response(client, task, user_text):
    """Send a learning task to the AI and return its response."""
    instructions = {
        "1": "Explain the topic for a beginner. Use a simple example and keep it concise.",
        "2": "Create a short beginner quiz with 3 questions about the topic, then show an answer key.",
        "3": "Summarize the notes into a few clear bullet points and list any key terms.",
    }
    response = client.responses.create(
        model=MODEL,
        instructions=instructions[task],
        input=user_text,
    )
    return response.output_text


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set. Add it to your environment, then run this program again.")
        return

    client = OpenAI()
    print("AI Study Buddy")
    print("Choose an option:")
    print("1. Explain a topic")
    print("2. Make a short quiz")
    print("3. Summarize notes")
    task = input("Enter 1, 2, or 3: ").strip()
    if task not in {"1", "2", "3"}:
        print("Please choose 1, 2, or 3.")
        return

    if task == "3":
        user_text = input("Paste your notes: ").strip()
    else:
        user_text = input("What topic should we work on? ").strip()
    if not user_text:
        print("Please enter a topic or some notes.")
        return

    try:
        print("\nWorking...\n")
        print(get_ai_response(client, task, user_text))
    except Exception as error:
        print(f"The request did not complete: {error}")
        print("Check your internet connection, API key, and account access, then try again.")


if __name__ == "__main__":
    main()
