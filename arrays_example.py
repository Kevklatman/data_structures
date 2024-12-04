"""
Interactive Array Learning CLI
----------------------------
A hands-on way to learn about arrays (lists) in Python
"""

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def print_array(arr, message="Current array:"):
    print(f"\n{message}")
    print(f"Array: {arr}")
    print(f"Indices: {[i for i in range(len(arr))]}")

def get_valid_index(arr, purpose=""):
    while True:
        try:
            index = int(input(f"Enter an index {purpose} (0-{len(arr)-1}): "))
            if 0 <= index < len(arr):
                return index
            print(f"Index must be between 0 and {len(arr)-1}")
        except ValueError:
            print("Please enter a valid number")

def guided_array_tutorial():
    clear_screen()
    print("\n=== Welcome to the Array Tutorial! ===")
    print("This tutorial will walk you through the fundamental concepts of arrays.")
    input("\nPress Enter to begin...")

    # Introduction
    clear_screen()
    print("\n1. What is an Array?")
    print("-----------------")
    print("An array is a collection of elements stored at contiguous memory locations.")
    print("In Python, we implement arrays using lists, which are more flexible than traditional arrays.")
    print("They can store elements of different types and can grow or shrink dynamically.")
    input("\nPress Enter to continue...")

    # Creating Arrays
    clear_screen()
    print("\n2. Creating Arrays")
    print("----------------")
    example_array = [1, 2, 3, 4, 5]
    print("We can create an array like this: example_array = [1, 2, 3, 4, 5]")
    print(f"Our array: {example_array}")
    print("\nEach element has an index, starting from 0:")
    print_array(example_array)
    input("\nPress Enter to continue...")

    # Accessing Elements
    clear_screen()
    print("\n3. Accessing Elements")
    print("-------------------")
    print("We can access any element instantly using its index.")
    print(f"example_array[0] gives us: {example_array[0]} (first element)")
    print(f"example_array[2] gives us: {example_array[2]} (third element)")
    print("\nTime Complexity: O(1) - This means it's instant, regardless of array size!")
    input("\nPress Enter to continue...")

    # Modifying Elements
    clear_screen()
    print("\n4. Modifying Elements")
    print("-------------------")
    print("Before modification:", example_array)
    example_array[2] = 10
    print("After example_array[2] = 10:", example_array)
    print("\nTime Complexity: O(1) - Also instant!")
    input("\nPress Enter to continue...")

    # Adding Elements
    clear_screen()
    print("\n5. Adding Elements")
    print("----------------")
    print("There are two main ways to add elements:")
    print("\na) Append (add to end):")
    example_array.append(6)
    print(f"After append(6): {example_array}")
    print("Time Complexity: O(1) - Usually instant!")
    
    print("\nb) Insert (add at specific position):")
    example_array.insert(1, 7)
    print(f"After insert(1, 7): {example_array}")
    print("Time Complexity: O(n) - Needs to shift elements!")
    input("\nPress Enter to continue...")

    # Removing Elements
    clear_screen()
    print("\n6. Removing Elements")
    print("------------------")
    print(f"Current array: {example_array}")
    popped = example_array.pop()
    print(f"After pop(): {example_array} (removed {popped})")
    print("Time Complexity: O(1) - Instant for last element")
    
    popped = example_array.pop(1)
    print(f"After pop(1): {example_array} (removed {popped})")
    print("Time Complexity: O(n) - Needs to shift elements when removing from middle")
    input("\nPress Enter to continue...")

    # Searching
    clear_screen()
    print("\n7. Searching")
    print("-----------")
    search_value = 4
    print(f"Current array: {example_array}")
    print(f"Searching for {search_value}...")
    if search_value in example_array:
        index = example_array.index(search_value)
        print(f"Found {search_value} at index {index}")
    print("\nTime Complexity: O(n) - Might need to check every element")
    input("\nPress Enter to continue...")

    # Slicing
    clear_screen()
    print("\n8. Slicing")
    print("----------")
    print(f"Current array: {example_array}")
    print("Slicing lets us get a portion of the array")
    print(f"First two elements (array[0:2]): {example_array[0:2]}")
    print(f"Last two elements (array[-2:]): {example_array[-2:]}")
    print(f"Middle elements (array[1:-1]): {example_array[1:-1]}")
    input("\nPress Enter to continue...")

    # Conclusion
    clear_screen()
    print("\n=== Tutorial Complete! ===")
    print("\nYou've learned about:")
    print("✓ Array basics and creation")
    print("✓ Accessing and modifying elements")
    print("✓ Adding and removing elements")
    print("✓ Searching and slicing")
    print("\nFeel free to practice these concepts using the other menu options!")
    input("\nPress Enter to return to main menu...")

def interactive_array_learning():
    array = [1, 2, 3, 4, 5]  # Starting with a simple array
    
    while True:
        clear_screen()
        print("\n=== Array Learning Interactive CLI ===")
        print_array(array)
        print("\nOperations:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Add element to end (append)")
        print("4. Insert element at position")
        print("5. Remove last element")
        print("6. Remove element at position")
        print("7. Search for element")
        print("8. Array slicing")
        print("9. Create new array")
        print("10. Quiz me!")
        print("11. Guided Tutorial")
        print("0. Exit")

        choice = input("\nChoose an operation (0-11): ")

        if choice == "0":
            print("\nThanks for learning about arrays! Keep practicing!")
            break

        elif choice == "1":
            print_array(array)
            index = get_valid_index(array)
            print(f"\nElement at index {index} is: {array[index]}")
            print("\nTime Complexity: O(1) - Instant access!")
            
        elif choice == "2":
            print_array(array)
            index = get_valid_index(array)
            try:
                new_value = int(input("Enter new value: "))
                array[index] = new_value
                print(f"\nModified array at index {index}")
                print("\nTime Complexity: O(1) - Instant modification!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "3":
            try:
                value = int(input("Enter value to append: "))
                array.append(value)
                print("\nTime Complexity: O(1) - Usually constant time!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "4":
            print_array(array)
            try:
                position = int(input(f"Enter position (0-{len(array)}): "))
                value = int(input("Enter value to insert: "))
                array.insert(position, value)
                print("\nTime Complexity: O(n) - Need to shift elements!")
            except ValueError:
                print("Please enter valid numbers")

        elif choice == "5":
            if array:
                popped = array.pop()
                print(f"\nRemoved element: {popped}")
                print("\nTime Complexity: O(1) - Constant time!")
            else:
                print("\nArray is empty!")

        elif choice == "6":
            if array:
                print_array(array)
                index = get_valid_index(array)
                popped = array.pop(index)
                print(f"\nRemoved element at index {index}: {popped}")
                print("\nTime Complexity: O(n) - Need to shift elements!")
            else:
                print("\nArray is empty!")

        elif choice == "7":
            try:
                value = int(input("Enter value to search for: "))
                if value in array:
                    index = array.index(value)
                    print(f"\nFound {value} at index {index}")
                else:
                    print(f"\n{value} not found in array")
                print("\nTime Complexity: O(n) - Need to check each element!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "8":
            print_array(array)
            try:
                start = int(input("Enter start index (or press Enter for start): ") or "0")
                end = int(input("Enter end index (or press Enter for end): ") or str(len(array)))
                sliced = array[start:end]
                print(f"\nSliced array [{start}:{end}]: {sliced}")
            except ValueError:
                print("Please enter valid numbers")

        elif choice == "9":
            try:
                input_str = input("Enter numbers separated by spaces: ")
                array = [int(x) for x in input_str.split()]
                print("\nCreated new array!")
            except ValueError:
                print("Please enter valid numbers separated by spaces")

        elif choice == "10":
            questions = [
                ("What is the time complexity of accessing an element by index?", "O(1)"),
                ("What is the time complexity of inserting at a specific position?", "O(n)"),
                ("What is the time complexity of appending to the end?", "O(1)"),
                ("What is the time complexity of searching for an element?", "O(n)")
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

        elif choice == "11":
            guided_array_tutorial()

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_array_learning()
