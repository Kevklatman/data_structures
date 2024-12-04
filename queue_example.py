"""
Interactive Queue Learning CLI
----------------------------
A hands-on way to learn about queues in Python
"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_queue(self):
        if self.is_empty():
            return "Empty queue"
        return " <- ".join([str(item) for item in self.items])

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def simulate_print_queue():
    print_queue = Queue()
    print("\nSimulating Printer Queue:")
    print("1. Add print job (e.g., 'document1.pdf')")
    print("2. Type 'print' to process next job")
    print("3. Type 'done' when finished")
    
    while True:
        action = input("\nEnter action: ").lower()
        if action == 'done':
            break
        elif action == 'print':
            job = print_queue.dequeue()
            if job:
                print(f"Printing: {job}")
            else:
                print("No jobs in queue!")
        else:
            print_queue.enqueue(action)
            print(f"Added job to queue: {action}")
        
        print("\nPrint queue (front to back):")
        print(print_queue.print_queue())

def guided_queue_tutorial():
    clear_screen()
    print("\n=== Welcome to the Queue Tutorial! ===")
    print("This tutorial will walk you through the fundamental concepts of queues.")
    input("\nPress Enter to begin...")

    # Introduction
    clear_screen()
    print("\n1. What is a Queue?")
    print("----------------")
    print("A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.")
    print("Think of it like a line of people waiting:")
    print(" - New people join at the back of the line")
    print(" - People leave from the front of the line")
    print(" - The first person to arrive is the first person to leave")
    input("\nPress Enter to continue...")

    # Creating a Queue
    clear_screen()
    print("\n2. Creating a Queue")
    print("----------------")
    queue = Queue()
    print("We start with an empty queue:")
    print(queue.print_queue())
    print("\nLet's add some elements:")
    queue.enqueue("First")
    print("\nAfter enqueueing 'First':")
    print(queue.print_queue())
    queue.enqueue("Second")
    print("\nAfter enqueueing 'Second':")
    print(queue.print_queue())
    print("\nNotice how new elements go to the back!")
    input("\nPress Enter to continue...")

    # Basic Operations
    clear_screen()
    print("\n3. Basic Queue Operations")
    print("----------------------")
    print("Current queue:")
    print(queue.print_queue())
    
    print("\na) Enqueue (add to back):")
    queue.enqueue("Third")
    print("After enqueue('Third'):")
    print(queue.print_queue())
    print("Time Complexity: O(1) - Always adds to back!")
    
    print("\nb) Dequeue (remove from front):")
    dequeued = queue.dequeue()
    print(f"Dequeued value: {dequeued}")
    print("Queue after dequeue:")
    print(queue.print_queue())
    print("Time Complexity: O(1) - Always removes from front!")
    
    print("\nc) Front (view front element):")
    front = queue.front()
    print(f"Front element: {front}")
    print("Queue unchanged after front:")
    print(queue.print_queue())
    print("Time Complexity: O(1) - Just looking at front!")
    input("\nPress Enter to continue...")

    # Real-World Example
    clear_screen()
    print("\n4. Real-World Example: Printer Queue")
    print("--------------------------------")
    print("Queues are perfect for managing print jobs:")
    
    printer = Queue()
    print("\nLet's add some print jobs:")
    printer.enqueue("report.pdf")
    printer.enqueue("image.jpg")
    printer.enqueue("document.docx")
    print("\nPrinter queue:")
    print(printer.print_queue())
    
    print("\nProcessing first job...")
    job = printer.dequeue()
    print(f"Printing: {job}")
    print("\nRemaining queue:")
    print(printer.print_queue())
    input("\nPress Enter to continue...")

    # Common Use Cases
    clear_screen()
    print("\n5. Common Use Cases")
    print("----------------")
    print("Queues are used in many scenarios:")
    print("1. Print job spooling")
    print("2. Process scheduling in operating systems")
    print("3. Breadth-first search in graphs")
    print("4. Customer service systems")
    print("5. Message queues in distributed systems")
    input("\nPress Enter to continue...")

    # Advantages and Limitations
    clear_screen()
    print("\n6. Advantages & Limitations")
    print("-------------------------")
    print("Advantages:")
    print("✓ Perfect for FIFO scenarios")
    print("✓ All operations are O(1)")
    print("✓ Fair processing order")
    print("\nLimitations:")
    print("× Can only access front element")
    print("× No random access to elements")
    print("× May need size limit in practice")
    input("\nPress Enter to continue...")

    # Conclusion
    clear_screen()
    print("\n=== Tutorial Complete! ===")
    print("\nYou've learned about:")
    print("✓ Queue concepts and FIFO principle")
    print("✓ Basic operations (enqueue, dequeue, front)")
    print("✓ Real-world applications")
    print("✓ Advantages and limitations")
    print("\nFeel free to practice these concepts using the other menu options!")
    input("\nPress Enter to return to main menu...")

def interactive_queue_learning():
    queue = Queue()
    
    while True:
        clear_screen()
        print("\n=== Queue Learning Interactive CLI ===")
        print("\nCurrent queue (front to back):")
        print(queue.print_queue())
        print("\nOperations:")
        print("1. Enqueue (add to back)")
        print("2. Dequeue (remove from front)")
        print("3. View front")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Create new queue")
        print("7. Quiz me!")
        print("8. Simulate printer queue")
        print("9. Guided Tutorial")
        print("0. Exit")

        choice = input("\nChoose an operation (0-9): ")

        if choice == "0":
            print("\nThanks for learning about queues! Keep practicing!")
            break

        elif choice == "1":
            try:
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print("\nTime Complexity: O(1) - Adding to back!")
            except ValueError:
                print("Please enter a valid value")

        elif choice == "2":
            dequeued = queue.dequeue()
            if dequeued is not None:
                print(f"\nDequeued value: {dequeued}")
                print("Time Complexity: O(1) - Removing from front!")
            else:
                print("\nQueue is empty!")

        elif choice == "3":
            front = queue.front()
            if front is not None:
                print(f"\nFront value: {front}")
                print("Time Complexity: O(1) - Just looking at front!")
            else:
                print("\nQueue is empty!")

        elif choice == "4":
            print(f"\nQueue is {'empty' if queue.is_empty() else 'not empty'}")
            print("Time Complexity: O(1) - Just checking size!")

        elif choice == "5":
            print(f"\nQueue size: {queue.size()}")
            print("Time Complexity: O(1) - Maintaining size variable!")

        elif choice == "6":
            queue = Queue()
            try:
                input_str = input("Enter elements separated by spaces (first will be front): ")
                for x in input_str.split():
                    queue.enqueue(x)
                print("\nCreated new queue!")
            except ValueError:
                print("Please enter valid values separated by spaces")

        elif choice == "7":
            questions = [
                ("What is the time complexity of enqueue operation?", "O(1)"),
                ("What is the time complexity of dequeue operation?", "O(1)"),
                ("What principle does a queue follow?", "FIFO"),
                ("What real-world example represents a queue?", "Line of people")
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
            simulate_print_queue()

        elif choice == "9":
            guided_queue_tutorial()

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_queue_learning()
