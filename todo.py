import argparse
import json

def valid_task_number(value):
    """Ensure the task number is a valid positive integer."""
    try:
        number = int(value)
        if number < 1:
            raise ValueError  # Ensure it's at least 1
        return number
    except ValueError:
        raise argparse.ArgumentTypeError("Please write a valid number.")
def load_tasks():
    """Function to load tasks from the file."""
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file doesn't exist or contains invalid JSON


def save_task(tasks):
    """Function to save tasks to the file."""
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)


def delete_task(tasks, task_number):
    """Function to delete tasks from the file."""
    new_tasks = [todo for i, todo in enumerate(tasks) if i != task_number - 1]
    save_task(new_tasks)
    print(f'The {task_number}. task was deleted successfully.')

def mark_task_completed(tasks, task_number):
    """Function to mark a task as completed."""

    if 1 <= task_number <= len(tasks):  # Validate task number
        tasks[task_number - 1]["completed"] = True
        save_task(tasks)
        print(f'The {task_number}. task was marked as completed.')
    else:
        print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")


# Argument Parsing
parser = argparse.ArgumentParser(description='Todo list with CLI.')
subparsers = parser.add_subparsers(dest="command")

# Add subcommand
add_parser = subparsers.add_parser("add", help="Adds tasks.")
delete_parser = subparsers.add_parser("delete", help="Removes tasks")
list_parser = subparsers.add_parser("list", help="Lists all tasks")
mark_parser = subparsers.add_parser("mark", help="Mark a task completed")


add_parser.add_argument("todo", type=str, help="The task to add.")
delete_parser.add_argument("task_nr", type=valid_task_number, help="Task number for deletion.")
mark_parser.add_argument("done_task_nr", type=valid_task_number, help="Task number of the done task.")
args = parser.parse_args()


if args.command == "add":
    data = {
        'task_name': args.todo,
        "completed": False
    }
    # Load tasks, append the new task, and save
    tasks = load_tasks()
    tasks.append(data)
    save_task(tasks)
    print(f'Task "{args.todo}" was added successfully!')
elif args.command == "list":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Please add tasks first.")
        print("Goodbye!")
        exit()
    else:
        print("\n📌 Your To-Do List:")
        for idx, job in enumerate(tasks, start=1):
            status = "[✅ ]" if job["completed"] else "[ ]"
            print(f"{idx}. {status} {job['task_name']}")

    # Handle next step (delete or exit)
    next_step = input("What do you want to do? Delete a task or exit? Write 'delete' or 'exit': ")

    while next_step.lower() not in ['delete', 'exit']:
        print("Invalid answer")
        next_step = input("Delete a task or exit? Write 'delete' or 'exit': ")

    if next_step.lower() == 'delete':


        while True:
            # Handle the case where there is only one task left
            if len(tasks) == 1:
                task_number = input("Please write the task number (1): ")
                # Immediately reject any input greater than 1 when there is only one task
                if task_number != '1':
                    print("There is just 1 task, other inputs are invalid, just write 1.")
                    continue
            else:
                task_number = input(f"Please write the task number between 1 and {len(tasks)}: ")

            try:
                task_number = int(task_number)
                if 1 <= task_number <= len(tasks): #checks if it's within the range of the tasks numbers
                    # Delete the task
                    delete_task(tasks, task_number)
                    break
                else:
                    print(f"Please enter a number between 1 and {len(tasks)}.")
            except ValueError:
                print('The variable is not a valid number.')

    elif next_step.lower() == 'exit':
        print("Goodbye!")
        exit()

elif args.command == "delete":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Please add tasks first.")
        print("Goodbye!")
        exit()
    else:
        # If there is only one task, we explicitly check and handle it differently
        if len(tasks) == 1:
            if args.task_nr == 1:
                delete_task(tasks, args.task_nr)
            else:
                print(f"Invalid task number. Please enter 1, since there is just 1 task.")
        else:
            # If there are multiple tasks, we check if the task number is within the valid range
            if 1 <= args.task_nr <= len(tasks):
                delete_task(tasks, args.task_nr)
            else:
                print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")

elif args.command == "mark":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Please add tasks first.")
        print("Goodbye!")
        exit()
    else:
        # If there is only one task, we explicitly check and handle it differently
        if len(tasks) == 1:
            if args.done_task_nr == 1:
                mark_task_completed(tasks, args.done_task_nr)
            else:
                print(f"Invalid task number. Please enter 1, since there is just 1 task.")
        else:
            # If there are multiple tasks, we check if the task number is within the valid range
            if 1 <= args.done_task_nr <= len(tasks):
                mark_task_completed(tasks, args.done_task_nr)
            else:
                print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")

