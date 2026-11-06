# Learning Notes: Introduction to AI & Python

## 1. Artificial Intelligence, Machine Learning, and Deep Learning

- **Artificial Intelligence (AI)** is the broad field of building computer systems that perform tasks associated with human intelligence, such as understanding language, recognizing images, planning, or making recommendations.
- **Machine Learning (ML)** is one approach within AI. Rather than writing every decision as a fixed rule, developers train a model to find patterns in examples and use those patterns to make predictions or decisions.
- **Deep Learning (DL)** is a family of ML methods based on neural networks with many layers. It often needs substantial data and computing resources and is used for tasks such as image recognition, speech, and modern language systems.

In short: **Deep Learning is part of Machine Learning, and Machine Learning is part of AI.** Not every AI system learns from data; a hand-written rule system can also be AI.

### A simple example

Imagine sorting messages into “spam” and “not spam.” A rule-based system might flag messages containing certain phrases. An ML system can learn patterns from examples already labelled as spam or not spam. A deep learning system could use a large neural network to learn more complex patterns from text. All three are approaches to the broader problem of classifying messages.

## 2. Real-world AI applications

- **Healthcare:** helping clinicians review scans or prioritize cases. These systems support professionals; they do not replace clinical judgment.
- **Transport:** estimating arrival times, planning routes, and helping driver-assistance systems detect nearby objects.
- **Shopping and media:** recommending products, music, or videos based on activity and preferences.
- **Banking:** identifying unusual transactions for further review.
- **Accessibility:** speech recognition, captions, text-to-speech, and image descriptions.
- **Customer support:** answering common questions or routing a request to the right team.

AI outputs can be wrong or biased. People should check important decisions, especially when they affect health, money, safety, or access to services.

## 3. Python foundations

### Variables and values

A variable is a name that refers to a value. Common types include integers (`int`), decimal numbers (`float`), text (`str`), and true/false values (`bool`).

```python
learner = "Sam"
lessons_completed = 3
progress = 0.75
is_learning = True
```

Use descriptive names. Python variable names are case-sensitive, and words such as `for` and `class` are reserved keywords.

### Lists

A list stores an ordered collection. Indexes start at zero.

```python
topics = ["variables", "loops", "functions"]
print(topics[0])  # variables
topics.append("lists")
```

### Loops

A `for` loop repeats once for each item in a collection. A `while` loop repeats as long as its condition is true.

```python
for topic in topics:
    print(topic)
```

### Functions

A function is a named, reusable block of code. Parameters let it receive input; `return` sends a result back.

```python
def greet(name):
    return f"Hello, {name}!"
```

### Input and output

`input()` reads text from the user. Convert it with `int()` or `float()` when numeric calculations are needed. `print()` displays a result.

## 4. Practice habits

1. Run a small example and observe its output.
2. Change one value at a time and predict what will happen.
3. Read error messages from the last line upward; check spelling, indentation, and data types.
4. Break a larger task into small functions with clear names.
5. Use sample data responsibly. Do not put passwords or private personal information into public repositories or AI tools.
