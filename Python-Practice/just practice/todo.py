import os

todo_list =[]; 

def add_to_list():
    task = input("Enter a task : ")
    todo_list.append(task)
    view_list()
    return

def view_list():
    print()
    for task in range(len(todo_list)):
        print(f"{task+1}. {todo_list[task]}")
    print()
    return

def mark_done():
    view_list()
    completed_task = int(input("Enter task Number to mark done and remove from list: "))
    print(f"Task Removed : {todo_list[(completed_task-1)]}")
    todo_list.remove(todo_list[(completed_task-1)])
    view_list()
    return

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")
    print("==========================")

def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        _ = os.system('cls')

def main():
    operation = 0
    while operation != -1:
        clear_screen()
        
        print("===== TO-DO LIST MENU =====")
        print("Enter 1 to add a task")
        print("Enter 2 to view the to-do list")
        print("Enter 3 to remove a task")
        print("Enter -1 to exit")
        print("==========================")

        try:
            operation = int(input("Enter choice: "))
            
            match(operation):
                case 1:
                    add_to_list()
                case 2:
                    view_list()
                    if operation != -1:
                        input("\nPress Enter to continue...")
                case 3:
                    mark_done()
                case -1:
                    print("Goodbye! 👋")
                    break 
                case _:
                    print("Invalid input, please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")


main()


