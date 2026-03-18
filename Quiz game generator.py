
import json
import os

FILENAME= "My scores.json"
name= input("Enter your name: ")

def save_scores(scores):
    with open("My scores.json", "w") as file:
        json.dump(scores, file)


def load_highest_scores():
    if os.path.exists(FILENAME):
        return json.load(open(FILENAME))
    try:
        with open("My scores.json", "r") as file:
            scores = json.load(file)
            return scores
    except FileNotFoundError:
        return {}


def subject_menu():
    print("---the quiz game generator".upper().center(50,"-"))
    print(f"Hi {name}, welcome to the Quiz Game Generator")
    print("What subject would you like to do")
    print("📚 1. General Knowledge")
    print("💻 2. IT & Computers")
    print("🧠 3. Science")
    print("🌍 4. Geography")
    print("🎬 5. Entertainment & Pop Culture")
    print("🪂 6. Exit")

def quiz_data():
    scores=load_highest_scores()
    print(f"Your highest score is {load_highest_scores()}:")

    while True:
        choice = input("Enter your choice (1-6: ")
        if choice == "1":
            general_knowledge=[{"q":"1. What is the capital of France?",
                                "o":["\nMadrid", "\nBerlin", "\nParis", "\nRome"],
                                "a": 3},

                               {"q": "1. What is the capital of France?",
                                "o": ["\nMadrid", "\nBerlin", "\nParis", "\nRome"],
                                "a": 3},
                               ]