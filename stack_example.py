"""
Interactive Stack Learning CLI
----------------------------
A hands-on way to learn about stacks in Python
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_stack(self):
        if self.is_empty():
            return "Empty stack"
        return "\n".join([f"{len(self.items) - i}. {item}" for i, item in enumerate(reversed(self.items))])

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def guided_stack_tutorial():
    clear_screen()
    print("\n=== Welcome to the Stack Tutorial! ===")
    print("This tutorial will walk you through the fundamental concepts of stacks.")
    input("\nPress Enter to begin...")

    # Introduction
    clear_screen()
    print("\n1. What is a Stack?")
    print("----------------")
    print("A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.")
    print("Think of it like a stack of plates:")
    print(" - You can only add plates to the top")
    print(" - You can only remove plates from the top")
    print(" - You can only see the top plate")
    input("\nPress Enter to continue...")

    # Creating a Stack
    clear_screen()
    print("\n2. Creating a Stack")
    print("----------------")
    stack = Stack()
    print("We start with an empty stack:")
    print(stack.print_stack())
    print("\nLet's add some elements:")
    stack.push("First")
    print("\nAfter pushing 'First':")
    print(stack.print_stack())
    stack.push("Second")
    print("\nAfter pushing 'Second':")
    print(stack.print_stack())
    print("\nNotice how new elements go on top!")
    input("\nPress Enter to continue...")

    # Basic Operations
    clear_screen()
    print("\n3. Basic Stack Operations")
    print("----------------------")
    print("Current stack:")
    print(stack.print_stack())
    
    print("\na) Push (add to top):")
    stack.push("Third")
    print("After push('Third'):")
    print(stack.print_stack())
    print("Time Complexity: O(1) - Always adds to top!")
    
    print("\nb) Pop (remove from top):")
    popped = stack.pop()
    print(f"Popped value: {popped}")
    print("Stack after pop:")
    print(stack.print_stack())
    print("Time Complexity: O(1) - Always removes from top!")
    
    print("\nc) Peek (view top):")
    top = stack.peek()
    print(f"Top element: {top}")
    print("Stack unchanged after peek:")
    print(stack.print_stack())
    print("Time Complexity: O(1) - Just looking at top!")
    input("\nPress Enter to continue...")

    # Real-World Example
    clear_screen()
    print("\n4. Real-World Example: Undo/Redo")
    print("-----------------------------")
    print("Stacks are perfect for implementing undo/redo:")
    
    actions = Stack()
    print("\nLet's perform some actions:")
    actions.push("Write 'Hello'")
    actions.push("Write 'World'")
    actions.push("Add exclamation")
    print("\nAction history (most recent first):")
    print(actions.print_stack())
    
    print("\nWhen we undo, we pop from the actions stack:")
    popped = actions.pop()
    print(f"Undid: {popped}")
    print("\nRemaining actions:")
    print(actions.print_stack())
    input("\nPress Enter to continue...")

    # Common Use Cases
    clear_screen()
    print("\n5. Common Use Cases")
    print("----------------")
    print("Stacks are used in many scenarios:")
    print("1. Browser history (back/forward)")
    print("2. Undo/Redo operations")
    print("3. Expression evaluation")
    print("4. Function call management (call stack)")
    print("5. Syntax parsing (matching parentheses)")
    input("\nPress Enter to continue...")

    # Advantages and Limitations
    clear_screen()
    print("\n6. Advantages & Limitations")
    print("-------------------------")
    print("Advantages:")
    print(" Simple and intuitive")
    print(" All operations are O(1)")
    print(" Perfect for LIFO scenarios")
    print("\nLimitations:")
    print(" Can only access top element")
    print(" No random access to elements")
    print(" Limited by size (if using array)")
    input("\nPress Enter to continue...")

    # Conclusion
    clear_screen()
    print("\n=== Tutorial Complete! ===")
    print("\nYou've learned about:")
    print(" Stack concepts and LIFO principle")
    print(" Basic operations (push, pop, peek)")
    print(" Real-world applications")
    print(" Advantages and limitations")
    print("\nFeel free to practice these concepts using the other menu options!")
    input("\nPress Enter to return to main menu...")

def interactive_stack_learning():
    stack = Stack()
    
    while True:
        clear_screen()
        print("\n=== Stack Learning Interactive CLI ===")
        print("\nCurrent stack (top to bottom):")
        print(stack.print_stack())
        print("\nOperations:")
        print("1. Push (add to top)")
        print("2. Pop (remove from top)")
        print("3. Peek (view top)")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Create new stack")
        print("7. Quiz me!")
        print("8. Simulate real-world example")
        print("9. Guided Tutorial")
        print("0. Exit")

        choice = input("\nChoose an operation (0-9): ")

        if choice == "0":
            print("\nThanks for learning about stacks! Keep practicing!")
            break

        elif choice == "1":
            try:
                value = input("Enter value to push: ")
                stack.push(value)
                print("\nTime Complexity: O(1) - Adding to top!")
            except ValueError:
                print("Please enter a valid value")

        elif choice == "2":
            popped = stack.pop()
            if popped is not None:
                print(f"\nPopped value: {popped}")
                print("Time Complexity: O(1) - Removing from top!")
            else:
                print("\nStack is empty!")

        elif choice == "3":
            top = stack.peek()
            if top is not None:
                print(f"\nTop value: {top}")
                print("Time Complexity: O(1) - Just looking at top!")
            else:
                print("\nStack is empty!")

        elif choice == "4":
            print(f"\nStack is {'empty' if stack.is_empty() else 'not empty'}")
            print("Time Complexity: O(1) - Just checking size!")

        elif choice == "5":
            print(f"\nStack size: {stack.size()}")
            print("Time Complexity: O(1) - Maintaining size variable!")

        elif choice == "6":
            stack = Stack()
            try:
                input_str = input("Enter elements separated by spaces (first will be bottom): ")
                for x in input_str.split():
                    stack.push(x)
                print("\nCreated new stack!")
            except ValueError:
                print("Please enter valid values separated by spaces")

        elif choice == "7":
            questions = [
                ("What is the time complexity of push operation?", "O(1)"),
                ("What is the time complexity of pop operation?", "O(1)"),
                ("What principle does a stack follow?", "LIFO"),
                ("What real-world example represents a stack?", "Stack of plates")
            ]
            score = 0
            for q, a in questions:
                answer = input(f"\n{q}\nYour answer: ").strip().upper()
                if answer == a.upper():
                    print("Correct! ")
                    score += 1
                else:
                    print(f"Not quite. The answer is {a}")
            print(f"\nYou got {score} out of {len(questions)} correct!")

        elif choice == "8":
            print("\nSimulating Undo/Redo Operations:")
            actions = Stack()
            undo_stack = Stack()
            
            print("\n1. Type some actions (e.g., 'write code', 'delete line')")
            print("2. Use 'undo' to undo last action")
            print("3. Type 'done' when finished")
            
            while True:
                action = input("\nEnter action: ").lower()
                if action == 'done':
                    break
                elif action == 'undo':
                    if not actions.is_empty():
                        undone = actions.pop()
                        undo_stack.push(undone)
                        print(f"Undid action: {undone}")
                    else:
                        print("Nothing to undo!")
                else:
                    actions.push(action)
                    undo_stack = Stack()  # Clear redo stack
                
                print("\nAction history (most recent first):")
                print(actions.print_stack())

        elif choice == "9":
            guided_stack_tutorial()

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_stack_learning()
