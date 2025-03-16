listOfTasks = []

def addTask():
    inputTask = input("Enter the task you'd like me to add to the list: ")
    listOfTasks.append(inputTask)
    print("Task has been successfully added to the list!")

def deleteTask():
    if not listOfTasks:
        print("There are no tasks to delete.\n")
        return

    print("Tasks:")
    for index, name in enumerate(listOfTasks, start=1):
        print(f"{index}. {name}")
        
    try:
        deleteTaskNumber = int(input("Enter the number of the task you want to delete: ")) - 1

        if 0 <= deleteTaskNumber < len(listOfTasks):
            removedTask = listOfTasks.pop(deleteTaskNumber)
            print(f"'{removedTask}' has been deleted!\n")
        else:
            print("That number is out of bounds.\n")
            
    except ValueError:
        print("Please enter a valid number.\n")

def listTasks():
    if listOfTasks:

        longest = max(len(f"{i+1}. {task}") for i, task in enumerate(listOfTasks))
        border = "#" * longest

        print("Here is the list of your tasks..")

        print(border)
        for index, name in enumerate(listOfTasks, start=1):
            print(f"{index}. {name}")
        print(border + "\n")

    else:
        print("No tasks to display.\n")

def run():
    initiator = True
    while initiator:
        userInput = input("""
1. Add a task
2. Delete a task
3. List tasks
4. Exit
Please select a number: """)

        intInput = int(userInput)

        if intInput == 1:
            addTask()
        
        elif intInput == 2:
            deleteTask()

        elif intInput == 3:
            listTasks()
        
        elif intInput == 4:
            print("Exiting ToDoApp..")
            initiator = False

if __name__ == '__main__':
    run()

