"""Two beginner-friendly programs using only the Python standard library."""


def run_quiz():
    questions = [
        ("What does AI stand for? ", "artificial intelligence"),
        ("Which is broader: AI, ML, or DL? ", "ai"),
        ("What keyword defines a Python function? ", "def"),
    ]
    score = 0
    for prompt, expected in questions:
        answer = input(prompt).strip().lower()
        if answer == expected:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The answer is {expected}.")
    print(f"You scored {score} out of {len(questions)}.")


def run_average_calculator():
    raw_scores = input("Enter scores separated by spaces (example: 80 92 88): ").split()
    try:
        scores = [float(value) for value in raw_scores]
    except ValueError:
        print("Please enter numbers separated by spaces.")
        return
    if not scores:
        print("Enter at least one score.")
        return
    print(f"Average: {sum(scores) / len(scores):.2f}")


def main():
    print("Choose a mini program:")
    print("1. AI & Python quiz")
    print("2. Average calculator")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        run_quiz()
    elif choice == "2":
        run_average_calculator()
    else:
        print("Please run the program again and choose 1 or 2.")


if __name__ == "__main__":
    main()
