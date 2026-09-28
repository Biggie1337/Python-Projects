import json


def add_task():
    task_title = input("Enter task title: ")
    priority = input("Enter priority (Low/Medium/High): ")

    priority_list = ["low", "medium", "high"]
    while priority.lower() not in priority_list:
        print("Invalid priority!")
        priority = input("Enter priority (Low/Medium/High)")
    priority = priority.lower().capitalize()
    
    category = input("Enter category: ")
    
    
    if not tasks:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    task = {"id": new_id, "title": task_title, "completed": False, "priority": priority, "category": category}
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
            print(f"{index}. {task['title']} - [{status}] - Priority: {task['priority']} - Category: {task['category']}")


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

def edit_task():
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks, start = 1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"
            print(f"{index}. {task['title']} - [{status}]")

        task_choice = int(input("Enter task number to edit: "))
        while task_choice < 1 or task_choice > len(tasks):
            print("There is no such task number!")
            task_choice = input("Enter task number to edit: ")
        tasks[task_choice - 1]['title'] =  input("Enter a new title: ")

        with open("task manager v2/tasks.json", "w") as file:
            json.dump(tasks, file, indent = 4)

def search_tasks():
    search = input("Enter a task to search: ")
    found = False

    for index, task in enumerate(tasks, start = 1):
        if search.lower() in task["title"].lower():
            print(f"{index}. {task['title']}")
            found = True

    if not found:
        print("No tasks found!")
    
def filter_tasks():
    print("1. Pending Tasks")
    print("2. Completed Tasks")
    print()
    found = False
    try:
        filter_choice = int(input("Enter filter number: "))
        print()
        while filter_choice < 1 or filter_choice > 2:
            print("Filter choice must be in the list!")
            filter_choice = int(input("Enter filter number: "))
        for index, task in enumerate(tasks, start = 1):
            if filter_choice == 1:
                if not task["completed"]:
                    print(f"{index}. {task['title']}")
                    found = True
            elif filter_choice == 2:
                if task["completed"]:
                    print(f"{index}. {task['title']}")
                    found = True
        if not found:
            if filter_choice == 1:
                print("No pending tasks")
            else:
                print("No completed tasks")
    except ValueError:
        print("Filter choice must be an integer!")

def show_statistics():
    found = False
    total = 0
    completed = []
    for task in tasks:
        if task["completed"]:
            completed.append(task["completed"])
            found = True
        else:
            found = True
        total += 1
    if not found:
        print("No tasks yet!")
    pending = total - len(completed)
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {sum(completed)}")
    print(f"Pending tasks: {pending}")

        
print("1. Add Task")
print("2. Show Tasks")
print("3. Complete Task")
print("4. Remove Task")
print("5. Edit Task")
print("6. Search Tasks")
print("7. Filter Tasks")
print("8. Statistics")
print("9. Exit")

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
            edit_task()
        elif choice == 6:
            search_tasks()
        elif choice == 7:
            filter_tasks()
        elif choice == 8:
            show_statistics()
        elif choice == 9:
            break
    except ValueError:
        print("Wrong Choice!")
