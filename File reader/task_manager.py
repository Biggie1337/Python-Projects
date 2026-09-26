def add_task():
    newTask = input("New Task: ")
    with open("File reader/tasks.txt","a") as file:
        file.write(newTask + "\n")

def show_tasks():
    try:
        with open("File reader/tasks.txt","r") as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print("No tasks yet!")

def remove_task():
    task_list = []
    try:
        with open("File reader/tasks.txt", "r") as file:
            task_list = file.readlines()
        for index,task in enumerate(task_list,start = 1):
            print(f"{index}. {task.strip()}")
    
        task_choice = int(input("Enter task number: "))
        if task_choice < 1 or task_choice > len(task_list):
            raise ValueError("Task choice not in the list!")
        task_list.pop(task_choice - 1)
    
        with open("File reader/tasks.txt", "w") as file:
            for task in task_list:
                file.write(task)
                        
    except ValueError as error:
        print(error)

print("1. Add Task")
print("2. Show Tasks")
print("3. Remove Task")
print("4. Exit")

while True:
    try:
        print()
        choice = int(input("Enter your choice: "))
        if choice == 1:    
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
           remove_task()
        elif choice == 4:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice!")


