import json


def add_task():
    task_title = input("Enter task title: ")
    new_id = None
    if not tasks:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    task = {"id": new_id, "title": task_title, "completed": False}
    tasks.append(task)
    with open("task manager v2/tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"
            print(f"{index}. {task['title']} - [{status}]")


def complete_task():
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"
            print(f"{index}. {task['title']} - [{status}]")
        try:
            task_complete = int(input("Enter a task to mark as completed: "))
            if task_complete < 1 or task_complete > len(tasks):
                print("Task index out of range")
            else:
                tasks[task_complete - 1]["completed"] = True
                with open("task manager v2/tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)
        except ValueError:
            print("Enter task number!")


def remove_task():
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"
            print(f"{index}. {task['title']} - [{status}]")
        try:
            task_remove = int(input("Enter a task to remove: "))
            if task_remove < 1 or task_remove > len(tasks):
                print("Task index out of range")
            else:
                tasks.pop(task_remove - 1)
                with open("task manager v2/tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)
        except ValueError:
            print("Enter task number!")


print("1. Add Task")
print("2. Show Tasks")
print("3. Complete Task")
print("4. Remove Task")
print("5. Exit")

tasks = []
with open("task manager v2/tasks.json", "r") as file:
    tasks = json.load(file)


while True:
    try:
        print()
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            break
    except ValueError:
        print("Wrong Choice!")
