#import and variables breakdown
import random
while True:
    random_number = random.randint(1, 100)
    attempts= 10

#new game intro
    print("\n---New game started---".upper())
    print("Hello welcome to number guessing game")
    print("You have 10 attempts to guess the secret number\nGood Luck")

#new while loop for input
    while attempts > 0:
        user_input= input("Guess the number from 1 to 100: ")

        if not user_input.isdigit():
            print("That is not a valid number, try again!")
            continue

        guess = int(user_input)
        attempts-=1

#Giving users final outcome
        if guess==random_number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif random_number < guess:
            print("Your guess is too high")
        elif random_number > guess:
            print("Your guess is too low")

        if guess != random_number:
            print(f"{attempts} attempts left")

        if attempts==0 and guess != random_number:
            print(f"Game Over \nYou are out of attempts, the secret number was {random_number}")

#play again option for user
    play_again = input("Would you like to play again? (y/n) ").lower()
    if play_again != "y" and play_again != "yes":
        print("Thanks for playing the guessing game,Good bye.")
        break