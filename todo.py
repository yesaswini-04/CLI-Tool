import argparse
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"
# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
# Add a task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📌 No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"❌ Task deleted: {removed_task}")
    else:
        print("⚠ Invalid task number.")
def main():
    parser = argparse.ArgumentParser(description="📝 Simple To-Do List CLI Tool")
    
    parser.add_argument("command", choices=["add", "view", "delete"], help="Command to execute")
    parser.add_argument("task", nargs="?", help="Task description (for add) or task number (for delete)", type=str)

    args = parser.parse_args()

    if args.command == "add":
        if args.task:
            add_task(args.task)
        else:
            print("⚠ Please provide a task to add.")

    elif args.command == "view":
        view_tasks()

    elif args.command == "delete":
        if args.task and args.task.isdigit():
            delete_task(int(args.task))
        else:
            print("⚠ Please provide a valid task number to delete.")

if __name__ == "__main__":
    main()
