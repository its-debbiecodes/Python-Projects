#import string and secrets
import string
import secrets

#function for generating the password
def generate_password(length):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password="".join(secrets.choice(all_characters) for _ in range(length))
    return password

#users input and results
print("Welcome to Password Generator".upper())

while True:
    try:
        password_length=input("\nHow long do you want your password? or press q to quit: ")
        if password_length=="q":
            break

        length=int(password_length)
        if length< 8:
            print("Please enter a length of at least 8 characters")
            continue

        new_password = generate_password(length)
        print(f"Your password:{new_password}")

#except for letters and invalid input
    except ValueError:
        print("Please enter a valid number")
        continue

#generate new password option for user
    generate_new=input("\nWould you like to generate a new password?(y/n): ".lower())
    if generate_new not in["y","yes"]:
        print("Stay safe.")
        break