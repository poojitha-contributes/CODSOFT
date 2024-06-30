class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} [{status}]"



import os
import pickle

TASKS_FILE = 'tasks.pkl'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as file:
            return pickle.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            tasks.append(Task(description))
            save_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].mark_done()
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        elif choice == '4':
            display_tasks(tasks)
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks.pop(task_num)
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



