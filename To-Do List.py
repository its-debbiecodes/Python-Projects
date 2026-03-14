
import os
import json

FILENAME = "To-Do List.json"
name = input("Please enter your name: ").title()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as f:
            tasks=json.load(f)
            return tasks
    except FileNotFoundError:
        return []


def show_menu():
    print("-----YOUR TO DO LISTS-----")
    print(f"Hi {name}, what would you like to do?!")
    print("1. View Tasks".capitalize())
    print("2. Add Tasks".capitalize())
    print("3. Remove Tasks".capitalize())
    print("4. Mark as done ✅".capitalize())
    print("5. Exit".capitalize())

def main():
    tasks=load_tasks()

    while True:
        clear_screen()
        show_menu()
        choice = input("Please enter your choice (1-5): ")
        if choice == "1":
            clear_screen()
            print(f"\n{name} task".title())

            if not tasks:
                print("Your tasks list is empty!")

            else:
                for index, item in enumerate(tasks, start=1):
                    print(f"{index}. {item}")
            input("Press enter to go back to continue...")

        elif choice == "2":
            new_task = input("Please enter a new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"{new_task} added to your tasks list")
            input("Press enter to go back to continue...")

        elif choice == "3":
            if not tasks:
                print("Your tasks list is empty!")
            else:
                for index, item in enumerate(tasks, start=1):
                    print(f"{index}. {item}")
                try:
                    task_num = int(input("Please enter the number of task you would like to remove: "))
                    removed_task=tasks.pop(task_num-1)
                    save_tasks(tasks)
                    print(f"{removed_task} removed from your tasks list")

                except (ValueError, IndexError) as e:
                    print(f"{e}:Please enter a valid number from your tasks list")
            input("Press enter to go back to continue...")

        elif choice == "4":
            if not tasks:
                print("Your tasks list is empty!")

            else:
                try:
                    task_num = int(input("Please enter the number of task you would like to mark as done: "))
                    if "✅" not in tasks[task_num-1]:
                        tasks[task_num - 1]+= "✅"
                        save_tasks(tasks)
                        print(f"{tasks[task_num-1]} marked as done in your tasks list")
                    else:
                        print(f" {tasks[task_num-1]} Already marked as done in your tasks list")
                except (ValueError, IndexError) as e:
                    print(f"{e}:Please enter a valid number from your tasks list")
            input("Press enter to go back to continue...")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid number (1-4)")
            break

if __name__ == "__main__":
    main()
else:
    show_menu()




