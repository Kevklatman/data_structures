"""
Interactive Linked List Learning CLI
----------------------------------
A hands-on way to learn about linked lists in Python
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def get_node_at_position(self, position):
        current = self.head
        count = 0
        while current:
            if count == position:
                return current
            count += 1
            current = current.next
        return None

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty list"

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def guided_linked_list_tutorial():
    clear_screen()
    print("\n=== Welcome to the Linked List Tutorial! ===")
    print("This tutorial will walk you through the fundamental concepts of linked lists.")
    input("\nPress Enter to begin...")

    # Introduction
    clear_screen()
    print("\n1. What is a Linked List?")
    print("----------------------")
    print("A linked list is a sequence of elements where each element points to the next element.")
    print("Unlike arrays, elements are not stored in contiguous memory locations.")
    print("Each element (node) contains:")
    print(" - Data (the value we want to store)")
    print(" - Next (a reference to the next node)")
    input("\nPress Enter to continue...")

    # Creating a Linked List
    clear_screen()
    print("\n2. Creating a Linked List")
    print("----------------------")
    ll = LinkedList()
    print("We start with an empty list: head -> None")
    ll.append(1)
    print("\nAfter adding 1:")
    print("head -> [1|next] -> None")
    ll.append(2)
    print("\nAfter adding 2:")
    print("head -> [1|next] -> [2|next] -> None")
    print("\nNotice how each node points to the next one!")
    input("\nPress Enter to continue...")

    # Adding Elements
    clear_screen()
    print("\n3. Adding Elements")
    print("----------------")
    print("There are three ways to add elements:")
    
    print("\na) Append (add to end):")
    print("Current:", ll.print_list())
    ll.append(3)
    print("After append(3):", ll.print_list())
    print("Time Complexity: O(n) - Need to traverse to the end!")
    
    print("\nb) Prepend (add to beginning):")
    ll.prepend(0)
    print("After prepend(0):", ll.print_list())
    print("Time Complexity: O(1) - Just update the head!")
    
    print("\nc) Insert after a position:")
    ll.insert_after(ll.get_node_at_position(1), 1.5)
    print("After insert_after(position 1, 1.5):", ll.print_list())
    print("Time Complexity: O(n) - Need to find the position first!")
    input("\nPress Enter to continue...")

    # Deleting Elements
    clear_screen()
    print("\n4. Deleting Elements")
    print("------------------")
    print("Current list:", ll.print_list())
    ll.delete_node(1.5)
    print("\nAfter deleting 1.5:", ll.print_list())
    print("\nTo delete a node, we:")
    print("1. Find the node to delete")
    print("2. Update the previous node's next pointer to skip the deleted node")
    print("Time Complexity: O(n) - Need to find the node!")
    input("\nPress Enter to continue...")

    # Accessing Elements
    clear_screen()
    print("\n5. Accessing Elements")
    print("-------------------")
    print("Current list:", ll.print_list())
    position = 2
    node = ll.get_node_at_position(position)
    print(f"\nValue at position {position}: {node.data}")
    print("\nUnlike arrays, we must traverse the list to find elements!")
    print("Time Complexity: O(n) - Need to traverse the list!")
    input("\nPress Enter to continue...")

    # Advantages and Disadvantages
    clear_screen()
    print("\n6. Advantages & Disadvantages")
    print("--------------------------")
    print("Advantages:")
    print("✓ Dynamic size - can grow and shrink")
    print("✓ Efficient insertion/deletion at beginning")
    print("✓ No need to shift elements")
    print("\nDisadvantages:")
    print("× No random access - must traverse")
    print("× Extra memory for next pointers")
    print("× Not cache-friendly (elements scattered in memory)")
    input("\nPress Enter to continue...")

    # Conclusion
    clear_screen()
    print("\n=== Tutorial Complete! ===")
    print("\nYou've learned about:")
    print("✓ Linked List structure and concepts")
    print("✓ Adding elements (append, prepend, insert)")
    print("✓ Deleting elements")
    print("✓ Accessing elements")
    print("✓ Advantages and disadvantages")
    print("\nFeel free to practice these concepts using the other menu options!")
    input("\nPress Enter to return to main menu...")

def interactive_linked_list_learning():
    linked_list = LinkedList()
    
    while True:
        clear_screen()
        print("\n=== Linked List Learning Interactive CLI ===")
        print(f"\nCurrent list: {linked_list.print_list()}")
        print("\nOperations:")
        print("1. Append node (at end)")
        print("2. Prepend node (at beginning)")
        print("3. Insert after position")
        print("4. Delete node")
        print("5. Find node at position")
        print("6. Create new list")
        print("7. Quiz me!")
        print("8. Guided Tutorial")
        print("0. Exit")

        choice = input("\nChoose an operation (0-8): ")

        if choice == "0":
            print("\nThanks for learning about linked lists! Keep practicing!")
            break

        elif choice == "1":
            try:
                value = int(input("Enter value to append: "))
                linked_list.append(value)
                print("\nTime Complexity: O(n) - Need to traverse to end!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "2":
            try:
                value = int(input("Enter value to prepend: "))
                linked_list.prepend(value)
                print("\nTime Complexity: O(1) - Just updating head!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "3":
            try:
                position = int(input("Enter position after which to insert: "))
                value = int(input("Enter value to insert: "))
                node = linked_list.get_node_at_position(position)
                if node:
                    linked_list.insert_after(node, value)
                    print("\nTime Complexity: O(1) for insertion, O(n) for finding position!")
                else:
                    print("Position not found!")
            except ValueError:
                print("Please enter valid numbers")

        elif choice == "4":
            try:
                value = int(input("Enter value to delete: "))
                linked_list.delete_node(value)
                print("\nTime Complexity: O(n) - Need to find the node!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "5":
            try:
                position = int(input("Enter position to find: "))
                node = linked_list.get_node_at_position(position)
                if node:
                    print(f"\nFound value {node.data} at position {position}")
                else:
                    print("Position not found!")
                print("\nTime Complexity: O(n) - Need to traverse!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "6":
            linked_list = LinkedList()
            try:
                input_str = input("Enter numbers separated by spaces: ")
                for x in input_str.split():
                    linked_list.append(int(x))
                print("\nCreated new linked list!")
            except ValueError:
                print("Please enter valid numbers separated by spaces")

        elif choice == "7":
            questions = [
                ("What is the time complexity of accessing an element by position?", "O(n)"),
                ("What is the time complexity of inserting at the beginning?", "O(1)"),
                ("What is the time complexity of inserting at the end?", "O(n)"),
                ("What is the main advantage of linked lists over arrays?", "Dynamic size and efficient insertion/deletion")
            ]
            score = 0
            for q, a in questions:
                answer = input(f"\n{q}\nYour answer: ").strip().upper()
                if answer == a.upper():
                    print("Correct! ✅")
                    score += 1
                else:
                    print(f"Not quite. The answer is {a}")
            print(f"\nYou got {score} out of {len(questions)} correct!")

        elif choice == "8":
            guided_linked_list_tutorial()

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_linked_list_learning()
