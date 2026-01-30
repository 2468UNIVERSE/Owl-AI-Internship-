# CLI To-Do List Application
# Description:
# This program allows users to manage daily tasks using
# a command-line interface. Users can add, view,
# complete, and delete tasks.


# Task class represents a single to-do item
class Task:
    def __init__(self, task_id, task_title):
        # Unique ID for the task
        self.task_id = task_id

        # Title or description of the task
        self.task_title = task_title

        # Status of the task (completed or not)
        self.completed = False

    # Mark the task as completed
    def mark_done(self):
        self.completed = True

    # String representation of the task
    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.task_id}] {self.task_title} - {status}"


# ToDoList class manages multiple tasks
class ToDoList:
    def __init__(self):
        # List to store all tasks
        self.tasks = []

        # Counter to assign unique task IDs
        self.next_id = 1

    # Add a new task to the list
    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    # Display all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nCurrent Tasks:")
        for task in self.tasks:
            print(task)

    # Mark a task as completed using task ID
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_done()
                print("Task marked as completed.")
                return
        print("Task not found.")

    # Delete a task using task ID
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")


# Main function to run the menu-driven program
def main():
    # Create ToDoList object
    todo = ToDoList()

    # Infinite loop until user chooses to exit
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        # Take user input
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            todo.add_task(title)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as done: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            print("Exiting To-Do List Application.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
