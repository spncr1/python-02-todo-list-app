print("--- TODO LIST APPLICATION ---")

todo_list = [] # initialize empty list to store our tasks in

while True:
    print()
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Clear Todo List")
    print("4. View Tasks")
    print("5. Quit Application")
    choice = int(input("Select an option: "))
    if choice == 1:
        print()
        print("--- ADD A TASK ---")
        task = input("What task would like to add to your todo list? ")
        todo_list.append(task)
        print(f"{task} was successfully added.")
        print("------------------")
    elif choice == 2:
        print()
        print("--- REMOVE A TASK ---")
        remove_task = int(input("Which task would you like to remove? "))
        if 0 <= remove_task < len(todo_list): # still don't understand how this works really
            todo_list.pop(remove_task) # probably need a bit more clarification on this too
            print(f"{remove_task} was successfully removed.")
        else:
            print("That task number doesn't exist on your todo list.")
        print("---------------------")
    elif choice == 3:
        print("--- CLEAR TODO LIST ---")
        todo_list.clear()
        print("Your todo list has been cleared for today.")
        print("-----------------------")
    elif choice == 4:
        print()
        print("--- YOUR TODO LIST ---")
        for i, task in enumerate(todo_list, start=1): # still need to understand how this works
            print(f"{i}. {task}") # this prints the task at each iteration in order based on when it was added to the todo_list
        print("----------------------")
    elif choice == 5:
        print("Thank you for using the TODO LIST Application. See you soon!")
        break
    else:
        print("Please select a valid option!")