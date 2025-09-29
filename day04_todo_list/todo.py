from storage import load_tasks, save_tasks

def todo():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")
        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    deleted = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Task '{deleted}' deleted!")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
