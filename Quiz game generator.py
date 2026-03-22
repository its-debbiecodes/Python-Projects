
#IMPORT FILES
import json
import os
from json import JSONDecodeError

#DICTIONARIES FOR SUBJECTS
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
                            "a": 1}
                            ]

it_and_computer = [{"q": "1. What does CPU stand for?",
                              "o": ["\nCentral Processing Unit", "\nCentral Process Unit", "\nComputer Personal Unit", "\nAll of the above"],
                              "a": 0},

                             {"q": "2. What does RAM do?",
                              "o": ["\nStores files permanently", "\nRuns the operating system only", "\nTemporarily stores data for quick access", "\nConnects to the internet"],
                              "a": 2},

                             {"q": "3. Which is an operating system?",
                              "o": ["\nMicrosoft Word", "\nWindows", "\nChrome", "\nExcel"],
                              "a": 1},

                             {"q": "4. What does HTTP stand for?",
                              "o": ["\nHyper Transfer Text Protocol", "\nHigh Transfer Text Protocol", "\nHyperText Transmission Process", "\nHyperText Transfer Protocol"],
                              "a": 3},

                             {"q": "5. What device connects you to the internet?",
                              "o": ["\nPrinter", "\nMonitor", "\nRouter", "\nKeyboard"],
                              "a": 2},

                             {"q": "6. What is a virus in computing?",
                              "o": ["\nHardware damage", "\nA type of software bug", "\nMalicious software", "\nInternet connection issue"],
                              "a": 2},

                             {"q": "7. What does “IP” in IP address stand for?",
                              "o": ["\nInternet Process", "\nInternal Protocol", "\nInformation Process", "\nInternet Protocol"],
                              "a": 1},

                             {"q": "8. What is software?",
                              "o": ["\nPhysical computer parts", "\nPrograms and applications", "\nInternet cables", "\nScreens and monitors"],
                              "a": 1},

                             {"q": "9. Which of these is a web browser?",
                              "o": ["\nLinux", "\nGoogle Chrome", "\nWindows", "\nAndroid"],
                              "a": 1},

                             {"q": "10. What is troubleshooting?",
                              "o": ["\nInstalling apps", "\nFixing problems in a system", "\nWriting code", "\nDesigning websites"],
                              "a": 1}
                             ]

science = [{"q": "1. What is the chemical symbol for gold??",
                            "o": ["\nAg", "\nAu", "\nFe", "\nGo"],
                            "a": 1},

                           {"q": "2. What planet is closest to the sun?",
                            "o": ["\nVenus", "\nMercury", "\nEarth", "\nMars"],
                            "a": 1},

                           {"q": "3. What part of the body pumps blood?",
                            "o": ["\nBrain", "\nLiver", "\nHeart", "\nLungs"],
                            "a": 2},

                           {"q": "4. What gas do plants absorb?",
                            "o": ["\nOxygen", "\nCarbon dioxide", "\nNitrogen", "\nHydrogen"],
                            "a": 1},

                           {"q": "5. What force pulls objects to Earth?",
                            "o": ["\nGravity", "\nMagnetism", "\nEnergy", "\nPressure"],
                            "a": 0},

                           {"q": "6. What is the freezing point of water?",
                            "o": ["\n0°C", "\n32°C", "\n100°C", "\n-10°C"],
                            "a": 0},

                           {"q": "7. What is the center of an atom called?",
                            "o": ["\nElectron", "\nProton", "\nNucleus", "\nNeutron"],
                            "a": 2},

                           {"q": "8. What type of energy is from the sun?",
                            "o": ["\nWind energy", "\nSolar energy", "\nNuclear energy","\nChemical energy"],
                            "a": 1},

                           {"q": "9. What organ helps you breathe?",
                            "o": ["\nHeart", "\nLungs", "\nBrain", "\nKidney"],
                            "a": 1},

                           {"q": "10. What is the largest organ in the human body?",
                            "o": ["\nLiver", "\nBrain", "\nSkin", "\nHeart"],
                            "a": 2}
                           ]

#RUN QUIZ FUNCTION
def run_quiz(subject, question_block):
    print(f"--- Welcome to {subject} quiz game")

    score = 0

    for block in question_block:
        print(f"\n{block['q']}")

        for i, o in enumerate(block["o"]):
            letter = chr(65 + i)
            print(f"{letter}.{o.strip()} ")

        user_input = input("What is the right option (A,B,C or D): ").upper().strip()
        if len(user_input) == 1 and "A" <= user_input <= "D":
            user_index = ord(user_input) - 65
            if user_index == block["a"]:
                print("✅ Correct!")
                score += 1

            else:
                correct_letter = chr(65 + block["a"])
                print(f"❌ That's wrong, Correct answer is {correct_letter}!")

        else:
            print("INVALID INPUT, COUNTED AS WRONG!")

    print(f"\nQuiz finished!\nYour final score is: {score}/{len(question_block)}")
    return score

#JSON FILE BREAKDOWN
FILENAME= "My scores.json"
name= input("Enter your name: ")

def save_scores(scores):
    with open("My scores.json", "w") as file:
        json.dump(scores, file)


def load_highest_scores():
    if os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)

    except FileNotFoundError, JSONDecodeError:
        return {}

#QUIZ GAME MENU
def subject_menu():
    print("---the quiz game generator".upper().center(50,"-"))
    print(f"Hi {name}, welcome to the Quiz Game Generator")
    print("What subject would you like to do")
    print("📚 1. General Knowledge")
    print("💻 2. IT & Computers")
    print("🧠 3. Science")
    print("🪂 4. Exit")

#MAIN GAME DATA
def quiz_data():
    all_scores=load_highest_scores()
    print(f"Your highest score is {load_highest_scores()}:")

    all_scores = load_highest_scores()
    print("---- High score board----".upper().center(50,"-"))
    print(f"General Knowledge: {all_scores.get('General Knowledge', 0)}")
    print(f"IT & Computers: {all_scores.get('IT & Computers', 0)}")
    print(f"Science: {all_scores.get('Science', 0)}")

    while True:
        subject_menu()
        choice= input("\nPick a quiz subject (1-4: ")

        if choice == "1":
            current_score=run_quiz("General Knowledge", general_knowledge)
            if current_score > all_scores.get("General Knowledge", 0):
                print(f"🌟 Your new high score is {current_score}.")
                all_scores["General Knowledge"] = current_score
                save_scores(all_scores)


        elif choice == "2":
            current_score=run_quiz("IT & Computers", it_and_computer)
            if current_score > all_scores.get("IT & Computers", 0):
                print(f"🌟 Your new high score is {current_score}.")
                all_scores["IT & Computers"] = current_score
                save_scores(all_scores)

        elif choice == "3":
            current_score=run_quiz("Science", science)
            if current_score > all_scores.get("Science", 0):
                print(f"🌟 Your new high score is {current_score}.")
                all_scores["Science"] = current_score
                save_scores(all_scores)

        elif choice == "4":
            print("Thank you for using Quiz game!")
            break

        else:
            print("INVALID INPUT, Choose an option (1-4)!")

            print("Press enter to continue...")

#FINAL
if __name__ == "__main__":
    quiz_data()
