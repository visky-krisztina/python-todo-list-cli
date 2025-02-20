import argparse
import json

parser = argparse.ArgumentParser(description='Todo list with CLI.')
subparsers = parser.add_subparsers(dest="command")

# Add subcommand
add_parser = subparsers.add_parser("add", help="Adds tasks.")
remove_parser = subparsers.add_parser("delete", help="Removes tasks")
edit_parser = subparsers.add_parser("edit", help="Edits tasks")
list_parser = subparsers.add_parser("list", help="Lists all tasks")

#The task argument
add_parser.add_argument("todo", type=str, help="The task to add.")

args = parser.parse_args()



if args.command == "add":
    # Define the data as a Python dictionary
    data = {
        'task_name': args.todo
    }
    # Writing data to a JSON file: first read the file in a list, append the task to the list, then write it into the file
    # Read existing tasks
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    # Append the new task
    tasks.append(data)

    # Write the updated list back to the file
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f'Task "{args.todo}" was added successfully!')
elif args.command == "list":
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
            if not tasks:
                print("No tasks found.")
            else:
                print("\n📌 Your To-Do List:")
                for idx, job in enumerate(tasks, start=1):
                    print(f"{idx}. {job['task_name']}")
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []