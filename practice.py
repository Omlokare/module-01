"""Guided Python examples for Module 01. Run with: python practice.py"""


def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to Python."


def average(numbers):
    """Return the mean of a non-empty list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    # Variables can hold different kinds of values.
    learner = "Om"
    hours_practiced = 2
    is_ready_to_learn = True
    print(f"Learner: {learner}; practice hours: {hours_practiced}; ready: {is_ready_to_learn}")

    # A list keeps related values together.
    topics = ["variables", "loops", "functions", "lists"]
    print("\nTopics to practice:")
    for number, topic in enumerate(topics, start=1):
        print(f"{number}. {topic}")

    # Call a function and display its returned result.
    print("\n" + greet(learner))

    scores = [80, 92, 88]
    print(f"Average practice score: {average(scores):.1f}")


if __name__ == "__main__":
    main()
