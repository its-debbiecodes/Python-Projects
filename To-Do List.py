
name = input("Please enter your name: ").title()
def show_menu():
    print("-----YOUR TO DO LISTS-----")
    print(f"Hi {name}, what would you like to do?!")
    print("1. View Tasks".capitalize())
    print("2. Add Tasks".capitalize())
    print("3. Remove Tasks".capitalize())
    print("4. Exit".capitalize())

def main():
    tasks=[

    ]

    while True:
        show_menu()
        choice = input("Please enter your choice (1-4): ")
        if choice == "1":
            print("\nYour task".title())

            if not tasks:
                print("Your tasks list is empty!")
                continue

            else:
                for index, item in enumerate(tasks, start=1):
                    print(f"{index}. {item}")

        elif choice == "2":
            new_task = input("Please enter a new task: ")
            tasks.append(new_task)

            print(f"{new_task} added to your tasks list")
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")

        elif choice == "3":
            if not tasks:
                print("Your tasks list is empty!")
                continue

            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")

            try:
                task_num = int(input("Please enter the number of task you would like to remove: "))
                removed_task=tasks.pop(task_num-1)
                print(f"{removed_task} removed from your tasks list")

            except (ValueError, IndexError) as e:
                print(f"{e}:Please enter a valid number from your tasks list")


        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid number (1-4)")
            continue

        again=input("Do you want to continue? (y/n): ").lower().strip()
        if again not in ["y","yes"]:
            print("Thank you for your time!")
            break

if __name__ == "__main__":
    main()
else:
    show_menu()




