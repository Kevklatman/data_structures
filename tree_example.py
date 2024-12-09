"""
Interactive Binary Tree Learning CLI
---------------------------------
A hands-on way to learn about binary trees in Python

Binary Tree Visualization:
-----------------------
       ┌──── 7 ────┐
       │           │
   ┌── 3 ──┐   ┌──9──┐
   │       │   │     │
   1       5   8    10
   
Traversals:
- Inorder   (Left→Root→Right): 1,3,5,7,8,9,10
- Preorder  (Root→Left→Right): 7,3,1,5,9,8,10
- Postorder (Left→Right→Root): 1,5,3,8,10,9,7

Operations:
- insert(data) : Add new node
- search(data) : Find node with data
- delete(data) : Remove node with data
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = Node(data)
                return
            if not node.right:
                node.right = Node(data)
                return
            queue.append(node.left)
            queue.append(node.right)

    def search(self, data):
        if not self.root:
            return False
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.data == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def print_tree(self):
        if not self.root:
            return "Empty tree"
        
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        def print_level(node, level, space_count):
            if not node:
                return
            if level == 1:
                print(" " * space_count + str(node.data), end="")
            elif level > 1:
                print_level(node.left, level - 1, space_count)
                print_level(node.right, level - 1, space_count)

        height = get_height(self.root)
        for i in range(1, height + 1):
            space_count = 2 ** (height - i)
            print_level(self.root, i, space_count)
            print()

    def inorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
        return result

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def guided_tree_tutorial():
    clear_screen()
    print("\n=== Welcome to the Binary Tree Tutorial! ===")
    print("This tutorial will walk you through the fundamental concepts of binary trees.")
    input("\nPress Enter to begin...")

    # Introduction
    clear_screen()
    print("\n1. What is a Binary Tree?")
    print("----------------------")
    print("A binary tree is a hierarchical data structure where:")
    print(" - Each node has at most two children (left and right)")
    print(" - Each node contains a value/data")
    print(" - The first node is called the root")
    print(" - Nodes with no children are called leaves")
    input("\nPress Enter to continue...")

    # Creating a Tree
    clear_screen()
    print("\n2. Creating a Binary Tree")
    print("----------------------")
    tree = BinaryTree()
    print("We start with an empty tree:")
    tree.print_tree()
    print("\nLet's add some nodes:")
    tree.insert(1)
    print("\nAfter inserting 1 (root):")
    tree.print_tree()
    tree.insert(2)
    tree.insert(3)
    print("\nAfter inserting 2 and 3:")
    tree.print_tree()
    print("\nNotice how nodes are added level by level, left to right!")
    input("\nPress Enter to continue...")

    # Tree Traversals
    clear_screen()
    print("\n3. Tree Traversals")
    print("---------------")
    print("Current tree:")
    tree.print_tree()
    print("\nThere are three main ways to traverse a tree:")
    
    print("\na) Inorder (Left-Root-Right):")
    print(f"Result: {tree.inorder_traversal()}")
    print("Used for getting sorted order in BST")
    
    print("\nb) Preorder (Root-Left-Right):")
    print(f"Result: {tree.preorder_traversal()}")
    print("Used for creating a copy of the tree")
    
    print("\nc) Postorder (Left-Right-Root):")
    print(f"Result: {tree.postorder_traversal()}")
    print("Used for deleting the tree")
    
    print("\nTime Complexity: O(n) - Must visit every node!")
    input("\nPress Enter to continue...")

    # Searching
    clear_screen()
    print("\n4. Searching in a Tree")
    print("-------------------")
    print("Current tree:")
    tree.print_tree()
    value = 2
    found = tree.search(value)
    print(f"\nSearching for {value}: {'Found' if found else 'Not found'}")
    print("\nSearch process:")
    print("1. Start at root")
    print("2. Check current node")
    print("3. Explore left and right subtrees")
    print("\nTime Complexity:")
    print("- O(n) for unbalanced tree")
    print("- O(log n) for balanced tree")
    input("\nPress Enter to continue...")

    # Real-World Example
    clear_screen()
    print("\n5. Real-World Example: File System")
    print("------------------------------")
    print("Binary trees can represent hierarchical structures:")
    
    fs_tree = BinaryTree()
    fs_tree.root = Node("/root")
    fs_tree.root.left = Node("/home")
    fs_tree.root.right = Node("/usr")
    fs_tree.root.left.left = Node("/home/user1")
    
    print("\nFile System Structure:")
    fs_tree.print_tree()
    print("\nDirectory Listing (using preorder):")
    print(fs_tree.preorder_traversal())
    input("\nPress Enter to continue...")

    # Common Use Cases
    clear_screen()
    print("\n6. Common Use Cases")
    print("----------------")
    print("Binary trees are used in many scenarios:")
    print("1. File systems")
    print("2. HTML/XML DOM")
    print("3. Database indexing")
    print("4. Decision trees")
    print("5. Game AI (minimax)")
    input("\nPress Enter to continue...")

    # Advantages and Limitations
    clear_screen()
    print("\n7. Advantages & Limitations")
    print("-------------------------")
    print("Advantages:")
    print("✓ Hierarchical data representation")
    print("✓ Efficient searching (in balanced trees)")
    print("✓ Natural recursive structure")
    print("\nLimitations:")
    print("× Can become unbalanced")
    print("× More complex than linear structures")
    print("× May waste space with unbalanced nodes")
    input("\nPress Enter to continue...")

    # Conclusion
    clear_screen()
    print("\n=== Tutorial Complete! ===")
    print("\nYou've learned about:")
    print("✓ Binary tree concepts and structure")
    print("✓ Tree traversal methods")
    print("✓ Searching in trees")
    print("✓ Real-world applications")
    print("✓ Advantages and limitations")
    print("\nFeel free to practice these concepts using the other menu options!")
    input("\nPress Enter to return to main menu...")

def interactive_tree_learning():
    tree = BinaryTree()
    
    while True:
        clear_screen()
        print("\n=== Binary Tree Learning Interactive CLI ===")
        print("\nCurrent tree:")
        tree.print_tree()
        print("\nOperations:")
        print("1. Insert node")
        print("2. Search for value")
        print("3. View traversals")
        print("4. Create new tree")
        print("5. Quiz me!")
        print("6. Simulate file system")
        print("7. Guided Tutorial")
        print("0. Exit")

        choice = input("\nChoose an operation (0-7): ")

        if choice == "0":
            print("\nThanks for learning about binary trees! Keep practicing!")
            break

        elif choice == "1":
            try:
                value = int(input("Enter value to insert: "))
                tree.insert(value)
                print("\nTime Complexity: O(log n) for balanced tree!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "2":
            try:
                value = int(input("Enter value to search: "))
                found = tree.search(value)
                print(f"\nValue {value} {'found' if found else 'not found'} in tree")
                print("Time Complexity: O(n) for unbalanced, O(log n) for balanced!")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "3":
            print("\nTree Traversals:")
            print(f"Inorder (Left-Root-Right): {tree.inorder_traversal()}")
            print(f"Preorder (Root-Left-Right): {tree.preorder_traversal()}")
            print(f"Postorder (Left-Right-Root): {tree.postorder_traversal()}")
            print("\nTime Complexity: O(n) - Must visit each node!")

        elif choice == "4":
            tree = BinaryTree()
            try:
                input_str = input("Enter numbers separated by spaces: ")
                for x in input_str.split():
                    tree.insert(int(x))
                print("\nCreated new tree!")
            except ValueError:
                print("Please enter valid numbers separated by spaces")

        elif choice == "5":
            questions = [
                ("What is the time complexity of searching in a balanced binary tree?", "O(log n)"),
                ("What is the time complexity of inserting in a balanced binary tree?", "O(log n)"),
                ("What are the three types of tree traversals?", "Inorder, Preorder, Postorder"),
                ("What is the maximum number of children a binary tree node can have?", "2")
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

        elif choice == "6":
            print("\nSimulating Simple File System:")
            fs_tree = BinaryTree()
            fs_tree.root = Node("/root")
            fs_tree.root.left = Node("/home")
            fs_tree.root.right = Node("/usr")
            fs_tree.root.left.left = Node("/home/user1")
            fs_tree.root.left.right = Node("/home/user2")
            fs_tree.root.right.left = Node("/usr/bin")
            fs_tree.root.right.right = Node("/usr/lib")
            
            print("\nFile System Structure:")
            fs_tree.print_tree()
            print("\nDirectory Listing (using preorder traversal):")
            print(fs_tree.preorder_traversal())

        elif choice == "7":
            guided_tree_tutorial()

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_tree_learning()
