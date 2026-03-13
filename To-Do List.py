
def show_menu():
    print("-----YOUR TO DO LISTS-----")
    name=input("Please enter your name: ")
    print(f"Welcome {name}, what would you like to do?!")
    print("1. View Tasks".capitalize())
    print("2. Add Tasks".capitalize())
    print("3. Remove Tasks".capitalize())
    print("4. Exit".capitalize())

def main():
    task=[]

    while True:
        show_menu()
        choice = input("Please enter your choice (1-4): ")
        if choice == "1":
            print("\nYour task".capitalize())

            if not task:
                print("Your tasks list is empty!")
                continue

            else:
                for index, task in enumerate(task):
                    print(f"{index}. {task}")

        elif choice == "2":
            new_task = input("Please enter a new task: ")
            task.append(new_task)

            print(f"{new_task} added to your tasks list")
            for index, task in enumerate(task):
                print(f"{index}. {task}")

        elif choice == "3":
            if not task:
                print("Your tasks list is empty!")
                continue

            for index, task in enumerate(task):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Please enter the number of task you would like to remove: "))
                removed_task=task.pop(task_num-1)
                print(f"{removed_task} removed from your tasks list")

            except (ValueError, IndexError) as e:
                print(f"{e}:Please enter a valid number from your tasks list")


        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid number (1-4)")
            continue

        again=input("Do you want to continue? (y/n): ".lower())
        if again not in ["y" and "yes"]:
            print("Thank you for your time!")
            break

if __name__ == "__main__":
    main()
else:
    show_menu()




