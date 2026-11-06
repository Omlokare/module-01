# Module 05: AI Tools & Mini Project

## AI Study Buddy

A small command-line study assistant that uses the OpenAI API to explain a topic, make a short quiz, or summarize notes. It gives a practical example of using an AI tool for learning and productivity.

## Setup

1. Install Python 3.10 or newer.
2. Install the project dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`. Do not paste the key into the source code or commit it to GitHub.
4. Run the app:

   ```bash
   python study_buddy.py
   ```

On Windows PowerShell, set the key for the current terminal with `$env:OPENAI_API_KEY="your-key"`. On macOS or Linux, use `export OPENAI_API_KEY="your-key"`.

## Features

- Explain a topic in beginner-friendly language
- Generate a short quiz from a topic
- Summarize notes pasted into the app
- Basic input validation and a clear message if the API key is missing

AI responses can be incorrect. Check important facts against reliable sources and avoid entering personal or confidential information.

## Learning connection

This project practices functions, loops, user input, environment variables, API calls, and responsible use of AI tools.
