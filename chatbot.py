import random
from datetime import datetime

# -------------------------------
# Data
# -------------------------------

jokes = [
    "Why do programmers prefer Python? Because it's easy to understand!",
    "Why did the computer get cold? It forgot to close Windows.",
    "Why do Java developers wear glasses? Because they don't C#?"
]

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Learning never exhausts the mind.",
    "Believe in yourself and keep coding!"
]

python_tips = [
    "Practice coding every day to improve your skills.",
    "Understand the logic before writing code.",
    "Debugging is a part of learning. Every error teaches something new."
]

facts = [
    "Python was created by Guido van Rossum in 1991.",
    "The first computer bug was an actual moth.",
    "Python is one of the most popular programming languages in the world."
]

# -------------------------------
# Welcome
# -------------------------------

print("=" * 55)
print("         BASIC CHATBOT")
print("=" * 55)

name = input("Enter your name: ").strip().title()

print(f"\n👋 Welcome, {name}!")
print("I'm your Python Basic Chatbot.")
print("Let's have a simple and interactive conversation.")
print("Type 'help' to see the available commands.\n")

# -------------------------------
# Chat Loop
# -------------------------------

while True:

    user = input(f"{name}: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]:
        print(" Hello! Nice to meet you.")

    # Asking about chatbot
    elif user in ["your name", "who are you"]:
        print(" I'm a rule-based chatbot developed using Python.")

    # User well-being
    elif user in ["how are you", "how are u"]:
        print(" I'm doing great. Thanks for asking!")

    # Date
    elif user == "date":
        print(" Today's Date:", datetime.now().strftime("%d-%m-%Y"))

    # Time
    elif user == "time":
        print("Current Time:", datetime.now().strftime("%I:%M %p"))

    # Joke
    elif user == "joke":
        print("😂", random.choice(jokes))

    # Quote
    elif user == "quote":
        print("💡", random.choice(quotes))

    # Python Tip
    elif user == "python":
        print("🐍", random.choice(python_tips))

    # Fun Fact
    elif user == "fact":
        print("📚", random.choice(facts))

    # Help Menu
    elif user == "help":
        print("\n" + "=" * 40)
        print(" AVAILABLE COMMANDS")
        print("=" * 40)
        print(" hello / hi / hey")
        print(" how are you")
        print(" your name")
        print(" date")
        print(" time")
        print(" joke")
        print(" quote")
        print(" python")
        print(" fact")
        print(" help")
        print(" bye")
        print("=" * 40 + "\n")

    # Exit
    elif user == "bye":
        print(f"\n Thank you for chatting with me, {name}!")
        print("👋 Have a wonderful day. Goodbye!")
        break

    # Unknown Input
    else:
        print("\n Sorry, I couldn't understand that.")
        print("💡 Type 'help' to view the available commands.\n")