
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
                                "a": 2},

                               {"q": "2. Which planet is known as the Red Planet?",
                                "o": ["\nVenus", "\nMars", "\nJupiter", "\nSaturn"],
                                "a": 1},

                               {"q": "3. Who wrote Romeo and Juliet?",
                                "o": ["\nCharles Dickens", "\nWilliam Shakespeare", "\nJane Austen", "\nMark Twain"],
                                "a": 1},

                               {"q": "4. What is the largest ocean on Earth?",
                                "o": ["\nPacific Ocean", "\nIndian Ocean", "\nAtlantic Ocean", "\nArctic Ocean"],
                                "a": 0},

                               {"q": "5. How many continents are there?",
                                "o": ["\n5", "\n6", "\n7", "\n8"],
                                "a": 2},

                               {"q": "6. What is the boiling point of water?",
                                "o": ["\n50°C", "\n100°C", "\n150°C", "\n200°C"],
                                "a": 1},

                               {"q": "7. Which country is famous for the pyramids?",
                                "o": ["\nMexico", "\nPeru", "\nEgypt", "\nIndia"],
                                "a": 2},

                               {"q": "8. What gas do humans need to breathe?",
                                "o": ["\nCarbon dioxide", "\nOxygen", "\nNitrogen", "\nHelium"],
                                "a": 1},

                               {"q": "9. What is the currency of the UK?",
                                "o": ["\nEuro", "\nDollar", "\nYen", "\nPound"],
                                "a": 3},

                               {"q": "10. What is H2O commonly known as?",
                                "o": ["\nSalt", "\nWater", "\nOxygen", "\nHydrogen"],
                                "a": 3},
                               ]