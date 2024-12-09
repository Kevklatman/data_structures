"""
Interactive Big O Notation Learning CLI
------------------------------------
A hands-on way to learn about time and space complexity

Time Complexity Visualization:
---------------------------
Complexity    Growth Rate    Visualization
O(1)         Constant       ▀
O(log n)     Logarithmic    ▀ █ ▄ ▁
O(n)         Linear         ▀ █ █ █
O(n log n)   Linearithmic   ▀ █ ██ ███
O(n²)        Quadratic      ▀ ██ ████ ████████
O(2ⁿ)        Exponential    ▀ ██ ████ ███████████████
"""

import time
import random
import os
import platform

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

class BigODemo:
    def __init__(self):
        self.data = []
        self.sorted_data = []
        
    def generate_data(self, size):
        self.data = [random.randint(1, 1000) for _ in range(size)]
        self.sorted_data = sorted(self.data)

    def constant_time_demo(self):
        """O(1) - Array Access"""
        if not self.data:
            return None
        start_time = time.time()
        result = self.data[0]
        end_time = time.time()
        return result, end_time - start_time

    def logarithmic_time_demo(self, target):
        """O(log n) - Binary Search"""
        if not self.sorted_data:
            return None
        start_time = time.time()
        left, right = 0, len(self.sorted_data) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if self.sorted_data[mid] == target:
                end_time = time.time()
                return mid, end_time - start_time
            elif self.sorted_data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        end_time = time.time()
        return -1, end_time - start_time

    def linear_time_demo(self, target):
        """O(n) - Linear Search"""
        if not self.data:
            return None
        start_time = time.time()
        
        for i, num in enumerate(self.data):
            if num == target:
                end_time = time.time()
                return i, end_time - start_time
        
        end_time = time.time()
        return -1, end_time - start_time

    def linearithmic_time_demo(self):
        """O(n log n) - Merge Sort"""
        if not self.data:
            return None
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        start_time = time.time()
        sorted_arr = merge_sort(self.data.copy())
        end_time = time.time()
        return sorted_arr, end_time - start_time

    def quadratic_time_demo(self):
        """O(n²) - Bubble Sort"""
        if not self.data:
            return None
            
        start_time = time.time()
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        end_time = time.time()
        return arr, end_time - start_time

    def exponential_time_demo(self, n):
        """O(2ⁿ) - Recursive Fibonacci"""
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        start_time = time.time()
        result = fibonacci(n)
        end_time = time.time()
        return result, end_time - start_time

def print_menu():
    print("\nBig O Notation Examples Menu:")
    print("1. O(1) - Constant Time Demo")
    print("2. O(log n) - Logarithmic Time Demo")
    print("3. O(n) - Linear Time Demo")
    print("4. O(n log n) - Linearithmic Time Demo")
    print("5. O(n²) - Quadratic Time Demo")
    print("6. O(2ⁿ) - Exponential Time Demo")
    print("7. Generate New Data")
    print("8. Clear Screen")
    print("9. Exit")

def interactive_big_o_learning():
    demo = BigODemo()
    demo.generate_data(1000)  # Initial data generation

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            result, time_taken = demo.constant_time_demo()
            print(f"\nO(1) - Constant Time")
            print(f"First element: {result}")
            print(f"Time taken: {time_taken:.8f} seconds")

        elif choice == '2':
            target = random.choice(demo.sorted_data)
            result, time_taken = demo.logarithmic_time_demo(target)
            print(f"\nO(log n) - Binary Search")
            print(f"Searching for {target}")
            print(f"Found at index: {result}")
            print(f"Time taken: {time_taken:.8f} seconds")

        elif choice == '3':
            target = random.choice(demo.data)
            result, time_taken = demo.linear_time_demo(target)
            print(f"\nO(n) - Linear Search")
            print(f"Searching for {target}")
            print(f"Found at index: {result}")
            print(f"Time taken: {time_taken:.8f} seconds")

        elif choice == '4':
            result, time_taken = demo.linearithmic_time_demo()
            print(f"\nO(n log n) - Merge Sort")
            print(f"First few sorted elements: {result[:5]}...")
            print(f"Time taken: {time_taken:.8f} seconds")

        elif choice == '5':
            result, time_taken = demo.quadratic_time_demo()
            print(f"\nO(n²) - Bubble Sort")
            print(f"First few sorted elements: {result[:5]}...")
            print(f"Time taken: {time_taken:.8f} seconds")

        elif choice == '6':
            n = int(input("Enter a number for Fibonacci (warning: values > 35 may take very long): "))
            result, time_taken = demo.exponential_time_demo(min(n, 35))
            print(f"\nO(2ⁿ) - Recursive Fibonacci")
            print(f"Fibonacci({n}) = {result}")
            print(f"Time taken: {time_taken:.8f} seconds")

        elif choice == '7':
            size = int(input("Enter size of data (recommended: 1000-10000): "))
            demo.generate_data(size)
            print(f"\nGenerated new random data of size {size}")

        elif choice == '8':
            clear_screen()

        elif choice == '9':
            print("\nThank you for learning about Big O notation!")
            break

        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_big_o_learning()
