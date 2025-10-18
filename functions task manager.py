def add_task(tasks): 
    name = input("Task name: ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due date (DD-MM-YYYY): ")
    
    tasks[name] = {
        "Priority": priority,
        "Due date": due_date
    }

    print("Task added")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")   
        for task, details in tasks.items():
            print(f"{task} \nPriority: {details['Priority']} \nDue Date: {details['Due date']}") 


def del_task(tasks):
    print("You are now discarding a task.")
    task = input("Enter the task you wish to discard: ")
    if task not in tasks:
        print("Task not found")
    else:
        del tasks[task] 
        print("Task discarded") 


def del_tasks(tasks):
    tasks.clear()
    print("All tasks discarded")


## Main program loop ##
tasks = {} 

while True: 
    print("Welcome to Task Manager! Would you like to...")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Discard a task")
    print("4. Discard all tasks")
    print("5. Exit")

    option = input("Please enter the number of your choice: ")  

    if option == "1":
        add_task(tasks)

    elif option == "2":
        view_tasks(tasks) 
        
    
    elif option == "3":
        del_task(tasks)    
        

    elif option == "4":
        del_tasks(tasks)

    elif option == "5":
        print("Goodbye!") 
        break

    else:
        print("Invalid option, please try again")  


    continue_choice = input("Would you like to continue? (yes/no): ").lower()
    if continue_choice != "yes":
        print("Goodbye!")
        break  