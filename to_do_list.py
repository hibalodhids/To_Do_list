todo_list = []

def show_task():
    print('\nTo-Do List Menu:')
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_task()
    choice = input("Select an option (1-4): ")

    if choice == '1':
        if not todo_list:
            print("Nothing")
        else:
            print("Your tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter your Task: ")
        todo_list.append(task)
        print("Task added successfully.")
    elif choice == '3':
        if not todo_list:
            print("Nothing")
        else:

            print("Your tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
        try:
            task_num = int(input("Enter your task number (1-4): "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully.")
        except ValueError:
            print("Invalid task number.")


    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")

