"""
Interactive Graph Learning CLI
----------------------------
A hands-on way to learn about graphs in Python

Graph Visualization:
-----------------
    A ────── B
    │ ╲      │
    │  ╲     │
    │   ╲    │
    │    ╲   │
    │     ╲  │
    C ────── D

Representations:
1. Adjacency List:  A → [B,C,D]
                    B → [A,D]
                    C → [A,D]
                    D → [B,C,A]

Operations:
- add_vertex(v)     : Add new vertex
- add_edge(v1, v2)  : Connect vertices
- remove_vertex(v)  : Remove vertex
- remove_edge(v1,v2): Remove connection
"""

from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
            
        self.graph[vertex1].append(vertex2)
        if not self.directed:
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if not self.directed and vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if not self.directed:
                    if (neighbor, vertex) not in edges:
                        edges.append((vertex, neighbor))
                else:
                    edges.append((vertex, neighbor))
        return edges

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        traversal = []

        while queue:
            vertex = queue.popleft()
            traversal.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

    def dfs(self, start_vertex, visited=None, traversal=None):
        if visited is None:
            visited = set()
        if traversal is None:
            traversal = []
            
        visited.add(start_vertex)
        traversal.append(start_vertex)

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, traversal)
        return traversal

    def print_graph(self):
        if not self.graph:
            return "Empty graph"
        
        result = []
        for vertex in self.graph:
            neighbors = " -> ".join(map(str, self.graph[vertex])) if self.graph[vertex] else "no neighbors"
            result.append(f"{vertex}: {neighbors}")
        return "\n".join(result)

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def simulate_social_network():
    print("\nSimulating Social Network:")
    social_graph = Graph()
    
    # Add some users and connections
    users = ["Alice", "Bob", "Charlie", "David", "Eve"]
    connections = [
        ("Alice", "Bob"), ("Bob", "Charlie"),
        ("Charlie", "David"), ("David", "Eve"),
        ("Eve", "Alice"), ("Alice", "Charlie")
    ]
    
    for user in users:
        social_graph.add_vertex(user)
    for user1, user2 in connections:
        social_graph.add_edge(user1, user2)
    
    print("\nSocial Network Structure:")
    print(social_graph.print_graph())
    
    start_user = "Alice"
    print(f"\nFriend Suggestions for {start_user} (using BFS):")
    print(" -> ".join(social_graph.bfs(start_user)))

def guided_graph_tutorial():
    clear_screen()
    print("\n=== Welcome to the Graph Tutorial! ===")
    print("This tutorial will walk you through the fundamental concepts of graphs.")
    input("\nPress Enter to begin...")

    # Introduction
    clear_screen()
    print("\n1. What is a Graph?")
    print("----------------")
    print("A graph is a collection of vertices (nodes) connected by edges.")
    print("Think of it like a social network:")
    print(" - People are vertices")
    print(" - Friendships are edges")
    print(" - Connections can be directed (following) or undirected (mutual friendship)")
    input("\nPress Enter to continue...")

    # Creating a Graph
    clear_screen()
    print("\n2. Creating a Graph")
    print("----------------")
    graph = Graph()
    print("We start with an empty graph:")
    print(graph.print_graph())
    
    print("\nLet's add some vertices and edges:")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")
    print("\nAfter adding vertices A, B and edge A-B:")
    print(graph.print_graph())
    
    graph.add_vertex("C")
    graph.add_edge("B", "C")
    print("\nAfter adding vertex C and edge B-C:")
    print(graph.print_graph())
    input("\nPress Enter to continue...")

    # Graph Types
    clear_screen()
    print("\n3. Types of Graphs")
    print("---------------")
    print("a) Undirected Graph (current):")
    print("- Edges have no direction")
    print("- If A connects to B, B connects to A")
    print(graph.print_graph())
    
    print("\nb) Directed Graph:")
    dir_graph = Graph(directed=True)
    dir_graph.add_edge("X", "Y")
    dir_graph.add_edge("Y", "Z")
    print("- Edges have direction")
    print("- If X connects to Y, Y might not connect to X")
    print(dir_graph.print_graph())
    input("\nPress Enter to continue...")

    # Graph Traversals
    clear_screen()
    print("\n4. Graph Traversals")
    print("----------------")
    graph.add_edge("A", "C")  # Add edge to create a cycle
    print("Current graph:")
    print(graph.print_graph())
    
    print("\na) Breadth-First Search (BFS):")
    print("- Explores neighbors before going deeper")
    print(f"BFS from A: {' -> '.join(graph.bfs('A'))}")
    print("- Uses a queue")
    print("- Good for finding shortest paths")
    
    print("\nb) Depth-First Search (DFS):")
    print("- Explores as far as possible before backtracking")
    print(f"DFS from A: {' -> '.join(graph.dfs('A'))}")
    print("- Uses recursion/stack")
    print("- Good for exploring paths")
    input("\nPress Enter to continue...")

    # Real-World Example
    clear_screen()
    print("\n5. Real-World Example: Social Network")
    print("--------------------------------")
    social = Graph()
    users = ["Alice", "Bob", "Charlie", "David"]
    for user in users:
        social.add_vertex(user)
    social.add_edge("Alice", "Bob")
    social.add_edge("Bob", "Charlie")
    social.add_edge("Charlie", "David")
    
    print("Social Network:")
    print(social.print_graph())
    print("\nFinding all connections from Alice:")
    print(f"BFS: {' -> '.join(social.bfs('Alice'))}")
    print("This shows the network of friends and friends-of-friends!")
    input("\nPress Enter to continue...")

    # Common Use Cases
    clear_screen()
    print("\n6. Common Use Cases")
    print("----------------")
    print("Graphs are used in many scenarios:")
    print("1. Social Networks")
    print("2. Road/Transportation Networks")
    print("3. Computer Networks")
    print("4. Recommendation Systems")
    print("5. Web Page Rankings")
    input("\nPress Enter to continue...")

    # Advantages and Limitations
    clear_screen()
    print("\n7. Advantages & Limitations")
    print("-------------------------")
    print("Advantages:")
    print("✓ Model real-world relationships")
    print("✓ Efficient path finding")
    print("✓ Flexible structure")
    print("\nLimitations:")
    print("× Can be complex to implement")
    print("× Memory intensive for dense graphs")
    print("× May have performance issues with large graphs")
    input("\nPress Enter to continue...")

    # Conclusion
    clear_screen()
    print("\n=== Tutorial Complete! ===")
    print("\nYou've learned about:")
    print("✓ Graph concepts and structure")
    print("✓ Different types of graphs")
    print("✓ Graph traversal methods")
    print("✓ Real-world applications")
    print("✓ Advantages and limitations")
    print("\nFeel free to practice these concepts using the other menu options!")
    input("\nPress Enter to return to main menu...")

def interactive_graph_learning():
    graph = Graph()
    
    while True:
        clear_screen()
        print("\n=== Graph Learning Interactive CLI ===")
        print("\nCurrent graph:")
        print(graph.print_graph())
        print("\nOperations:")
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Remove edge")
        print("4. BFS traversal")
        print("5. DFS traversal")
        print("6. Create new graph")
        print("7. Toggle directed/undirected")
        print("8. Quiz me!")
        print("9. Simulate social network")
        print("10. Guided Tutorial")
        print("0. Exit")

        choice = input("\nChoose an operation (0-10): ")

        if choice == "0":
            print("\nThanks for learning about graphs! Keep practicing!")
            break

        elif choice == "1":
            vertex = input("Enter vertex name: ")
            graph.add_vertex(vertex)
            print("\nTime Complexity: O(1) - Simple addition to adjacency list!")

        elif choice == "2":
            v1 = input("Enter first vertex: ")
            v2 = input("Enter second vertex: ")
            graph.add_edge(v1, v2)
            print("\nTime Complexity: O(1) - Simple addition to adjacency list!")

        elif choice == "3":
            v1 = input("Enter first vertex: ")
            v2 = input("Enter second vertex: ")
            graph.remove_edge(v1, v2)
            print("\nTime Complexity: O(E) - Need to search through edges!")

        elif choice == "4":
            if graph.get_vertices():
                start = input("Enter starting vertex for BFS: ")
                if start in graph.get_vertices():
                    print("\nBFS Traversal:")
                    print(" -> ".join(map(str, graph.bfs(start))))
                    print("\nTime Complexity: O(V + E) - Must visit all vertices and edges!")
                else:
                    print("\nVertex not found in graph!")
            else:
                print("\nGraph is empty!")

        elif choice == "5":
            if graph.get_vertices():
                start = input("Enter starting vertex for DFS: ")
                if start in graph.get_vertices():
                    print("\nDFS Traversal:")
                    print(" -> ".join(map(str, graph.dfs(start))))
                    print("\nTime Complexity: O(V + E) - Must visit all vertices and edges!")
                else:
                    print("\nVertex not found in graph!")
            else:
                print("\nGraph is empty!")

        elif choice == "6":
            graph = Graph(directed=graph.directed)
            print("\nCreated new empty graph!")

        elif choice == "7":
            graph.directed = not graph.directed
            print(f"\nGraph is now {'directed' if graph.directed else 'undirected'}!")

        elif choice == "8":
            questions = [
                ("What is the time complexity of BFS/DFS traversal?", "O(V + E)"),
                ("What data structure is used in BFS?", "Queue"),
                ("What data structure is used in DFS?", "Stack/Recursion"),
                ("What are the two common ways to represent a graph?", "Adjacency List/Matrix")
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

        elif choice == "9":
            simulate_social_network()

        elif choice == "10":
            guided_graph_tutorial()

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_graph_learning()
