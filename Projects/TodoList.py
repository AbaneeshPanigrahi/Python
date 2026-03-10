class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(self.tasks):
                print(i + 1, "-", task)
todo = TodoList()

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        todo.show_tasks()

    elif choice == "2":
        task = input("Enter task: ")
        todo.add_task(task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")