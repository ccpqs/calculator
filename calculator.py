while True:
    print("Welcome to Calculator. Choose an action from below.")

    print("Multiplication")
    print("Addition")
    print("Division")
    print("Subtraction")
    print("Exit")

    choice = input("Enter your choice: ")

    if choice.lower() == "multiplication": # makes it so text is converted to pure lowercase and executed, preventing unnecessary errors
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))

        print(f"Answer: {a*b}") # f strings allow you to print both text and actions by doing f"Something: {Action}" 

    elif choice.lower() == "division":
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))
        
        if b == 0:
            print("Math Error, Cannot divide by 0")
        else: print(f"Answer: {a/b}")

    elif choice.lower() == "addition":
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))

        print(f"Answer: {a+b}")

    elif choice.lower() == "subtraction":
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))

        print(f"Answer: {a-b}")
    
    elif choice.lower() == "exit":
        print("Goodbye!")
        break

    elif choice.lower() != "multiplication" or "division" or "addition" or "subtraction" or "exit": # there could be a better way to do this, like a list
        invalid_choice = input("Invalid Option, Would you like to try again? (Y/N)")
        if invalid_choice.lower() != "y":
            print("Goodbye!")
            break
    
    
    persistence_choice = input("Would you like to keep using the calculator? (Y/N)")
    if persistence_choice.lower() != "y":
        print("Goodbye!")
        break