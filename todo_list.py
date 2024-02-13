#initialized class
class TodoList:
    
    #default parameter
    def __init__(self):
        self.tasks = []

    #add task method
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    #remove task method
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully!")
        else:
            print(f"Task '{task}' not found in the list.")
   
    #view task method
    def view_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Todo List is empty.")

#main body of todo list
def main():
    todo_list = TodoList()

    #flag to run program while boolean is met
    while True:
        print("\nTodo List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        #requests input from user to then check conditions 1, 2, 3, or 4
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

#ensures script is only run in this file and not on import
if __name__ == "__main__":
    main()
