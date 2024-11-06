import sys

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)

# Function for Prim's Algorithm
def prim_mst(graph, nodes):
    num_vertices = len(graph)
    selected = {nodes[0]: True}  # Start from the first node (A)
    mst_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    mst_edges = []  # To store the MST edges
    total_weight = 0  # To store the total weight of the MST
    num_edges = 0

    while num_edges < num_vertices - 1:
        min_edge = sys.maxsize
        u = v = -1

        for i, u_node in enumerate(nodes):
            if u_node in selected:
                for j, v_node in enumerate(nodes):
                    if v_node not in selected and graph[u_node][v_node] > 0:  # Ensure there's a valid edge
                        if min_edge > graph[u_node][v_node]:
                            min_edge = graph[u_node][v_node]
                            u, v = i, j

        if u != -1 and v != -1:
            selected[nodes[v]] = True
            mst_matrix[u][v] = graph[nodes[u]][nodes[v]]
            mst_matrix[v][u] = graph[nodes[v]][nodes[u]]
            mst_edges.append((nodes[u], nodes[v], min_edge))  # Add edge to the MST
            total_weight += min_edge  # Add edge weight to the total weight
            num_edges += 1

    print("\nEdges in the MST:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} (weight {w})")
    print("Total weight of the MST:", total_weight)

    # Print the MST Matrix (Adjacency Matrix)
    print("\nMST Matrix (Adjacency Matrix):")
    for row in mst_matrix:
        print(" ".join(map(str, row)))

# Main Menu for Selection Sort and Prim's Algorithm
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Selection Sort")
        print("2. Prim's Algorithm for MST")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            selection_sort_menu()
        elif choice == '2':
            prim_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle Selection Sort input
def selection_sort_menu():
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    selection_sort(arr)

# Function to handle Prim's Algorithm input
def prim_menu():
    print("\n--- Prim's Algorithm ---")
    num_nodes = int(input("Enter the number of nodes: "))
    nodes = [input(f"Enter name for node {i+1}: ").strip() for i in range(num_nodes)]
    
    graph = {node: {node: 0 for node in nodes} for node in nodes}  # Initialize the graph with 0 weights

    print("\nEnter the edges (e.g., A B 4 for edge A-B with weight 4):")
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter edge (u v weight): ").split()
        weight = int(weight)
        if u in graph and v in graph:
            graph[u][v] = weight
            graph[v][u] = weight  # Undirected graph
    
    prim_mst(graph, nodes)

# Start the menu
if __name__ == "__main__":
    menu()
