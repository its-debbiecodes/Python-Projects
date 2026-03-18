
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
    print("🪂 4. Exit")

def quiz_data():
    scores=load_highest_scores()
    print(f"Your highest score is {load_highest_scores()}:")

    while True:
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
                            ],

        it_and_computer = [{"q": "1. What does CPU stand for?",
                              "o": ["\nCentral Processing Unit", "\nCentral Process Unit", "\nComputer Personal Unit", "\nAll of the above"],
                              "a": 2},

                             {"q": "2. What does RAM do?",
                              "o": ["\nStores files permanently", "\nRuns the operating system only", "\nTemporarily stores data for quick access", "\nConnects to the internet"],
                              "a": 1},

                             {"q": "3. Which is an operating system?",
                              "o": ["\nMicrosoft Word", "\nWindows", "\nChrome", "\nExcel"],
                              "a": 1},

                             {"q": "4. What does HTTP stand for?",
                              "o": ["\nHyper Transfer Text Protocol", "\nHigh Transfer Text Protocol", "\nHyperText Transmission Process", "\nHyperText Transfer Protocol"],
                              "a": 0},

                             {"q": "5. What device connects you to the internet?",
                              "o": ["\nPrinter", "\nMonitor", "\nRouter", "\nKeyboard"],
                              "a": 2},

                             {"q": "6. What is a virus in computing?",
                              "o": ["\nHardware damage", "\nA type of software bug", "\nMalicious software", "\nInternet connection issue"],
                              "a": 1},

                             {"q": "7. What does “IP” in IP address stand for?",
                              "o": ["\nInternet Process", "\nInternal Protocol", "\nInformation Process", "\nInternet Protocol"],
                              "a": 2},

                             {"q": "8. What is software?",
                              "o": ["\nPhysical computer parts", "\nPrograms and applications", "\nInternet cables", "\nScreens and monitors"],
                              "a": 1},

                             {"q": "9. Which of these is a web browser?",
                              "o": ["\nLinux", "\nGoogle Chrome", "\nWindows", "\nAndroid"],
                              "a": 3},

                             {"q": "10. What is troubleshooting?",
                              "o": ["\nInstalling apps", "\nFixing problems in a system", "\nWriting code", "\nDesigning websites"],
                              "a": 1}
                             ],

        science = [{"q": "1. What is the chemical symbol for gold??",
                            "o": ["\nAg", "\nAu", "\nFe", "\nGo"],
                            "a": 2},

                           {"q": "2. What planet is closest to the sun?",
                            "o": ["\nVenus", "\nMercury", "\nEarth", "\nMars"],
                            "a": 1},

                           {"q": "3. Which is an operating system?",
                            "o": ["\nMicrosoft Word", "\nWindows", "\nChrome", "\nExcel"],
                            "a": 1},

                           {"q": "4. What does HTTP stand for?",
                            "o": ["\nHyper Transfer Text Protocol", "\nHigh Transfer Text Protocol",
                                  "\nHyperText Transmission Process", "\nHyperText Transfer Protocol"],
                            "a": 0},

                           {"q": "5. What device connects you to the internet?",
                            "o": ["\nPrinter", "\nMonitor", "\nRouter", "\nKeyboard"],
                            "a": 2},

                           {"q": "6. What is a virus in computing?",
                            "o": ["\nHardware damage", "\nA type of software bug", "\nMalicious software",
                                  "\nInternet connection issue"],
                            "a": 1},

                           {"q": "7. What does “IP” in IP address stand for?",
                            "o": ["\nInternet Process", "\nInternal Protocol", "\nInformation Process",
                                  "\nInternet Protocol"],
                            "a": 2},

                           {"q": "8. What is software?",
                            "o": ["\nPhysical computer parts", "\nPrograms and applications", "\nInternet cables",
                                  "\nScreens and monitors"],
                            "a": 1},

                           {"q": "9. Which of these is a web browser?",
                            "o": ["\nLinux", "\nGoogle Chrome", "\nWindows", "\nAndroid"],
                            "a": 3},

                           {"q": "10. What is troubleshooting?",
                            "o": ["\nInstalling apps", "\nFixing problems in a system", "\nWriting code",
                                  "\nDesigning websites"],
                            "a": 1}
                           ]

        def run_quiz(subject,question_block):
            print(f"--- Welcome to {subject} quiz game")

            score=0

            for block in question_block:
                print(f"\n{block['q']}")

                for i, o in enumerate(block["o"]):
                    letter= chr(65+i)
                    print(f"{letter}.{o.strip()} ")


                user_input = input("What is the right option (A,B,C or D): ").upper().strip()
                if len(user_input)==1 and "A"<= user_input<="D":
                    user_index= ord(user_input)-65
                    if user_index == question_block["a"]:
                        print("✅ Correct!")
                        score+=1

                    else:
                        correct_letter = chr(65+question_block["a"])
                        print(f"❌ That's wrong, Correct answer is {correct_letter}!")

                else:
                    print("INVALID INPUT, COUNTED AS WRONG!")

            print(f"\nQuiz finished!\nYour final score is: {score}/{len(question_block)}")
            return score






