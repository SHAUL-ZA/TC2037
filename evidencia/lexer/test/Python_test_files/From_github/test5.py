class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_task(self, task, new_title, new_description, new_due_date):
        task.title = new_title
        task.description = new_description
        task.due_date = new_due_date

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("== Tasks ==")
        for task in self.tasks:
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print("---------------------")

def display_menu():
    print("== Task Manager Menu ==")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

def run_task_manager():
    task_manager = TaskManager()

    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            due_date = input("Enter the task due date: ")
            task = Task(title, description, due_date)
            task_manager.add_task(task)
            print("Task added successfully.")

        elif option == "2":
            title = input("Enter the title of the task to remove: ")
            task = task_manager.get_task(title)
            if task:
                task_manager.remove_task(task)
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif option == "3":
            title = input("Enter the title of the task to update: ")
            task = task_manager.get_task(title)
            if task:
                new_title = input("Enter the new title: ")
                new_description = input("Enter the new description: ")
                new_due_date = input("Enter the new due date: ")
                task_manager.update_task(task, new_title, new_description, new_due_date)
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif option == "4":
            task_manager.display_tasks()

        elif option == "5":
            print("Exiting the Task Manager.")
            break

        else:
            print("Invalid option. Please select a valid option.")

run_task_manager()
