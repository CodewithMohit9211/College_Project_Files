# Node Class
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add Task
    def add_task(self, task):
        new_node = Node(task)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Delete Task
    def delete_task(self, task):
        temp = self.head

        if temp and temp.task == task:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.task == task:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Task not found!")

    # Display Tasks
    def display(self):
        if self.head is None:
            print("To-Do List is Empty.")
            return

        temp = self.head
        print("\nTo-Do List:")
        while temp:
            print("->", temp.task)
            temp = temp.next

# Main Program
todo = LinkedList()

while True:
    print("\n----- MENU -----")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        todo.add_task(task)

    elif choice == 2:
        task = input("Enter Task to Delete: ")
        todo.delete_task(task)

    elif choice == 3:
        todo.display()

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
