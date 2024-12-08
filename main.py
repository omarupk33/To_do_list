tasks = []

def addTask():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")


def listTasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"Task #{i}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task '{taskToDelete}' deleted successfully.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")





if __name__ == '__main__':

    while True:
        print("\n")
        print("Please select one of the following options:")
        print("___________________________________________________________________________________________\n")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            addTask()
        elif choice == '2':
            deleteTask()
        elif choice == '3':
            listTasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")