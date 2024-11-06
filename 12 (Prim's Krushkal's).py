import sys

# Function for Prim's Algorithm
def prim_mst(graph, nodes):
    num_vertices = len(graph)
    selected = {nodes[0]: True}  # Start from the first node (A)
    mst_matrix = [[0] * num_vertices for _ in range(num_vertices)]
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
            num_edges += 1

    print("\nMST Matrix (Adjacency Matrix):")
    for row in mst_matrix:
        print(" ".join(map(str, row)))


# Class for Kruskal's Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store all edges in the format (weight, u, v)

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst = []
        self.graph.sort()  # Sort edges by weight
        parent = list(range(self.V))
        rank = [0] * self.V

        for w, u, v in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)

        total_weight = sum(w for _, _, w in mst)
        print("\nEdges in the MST:")
        for u, v, w in mst:
            print(f"{u} - {v} (weight {w})")
        print("Total weight of the MST:", total_weight)


# Main Menu Function
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Prim's Algorithm for MST")
        print("2. Kruskal's Algorithm for MST")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            prim_menu()
        elif choice == '2':
            kruskal_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


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


# Function to handle Kruskal's Algorithm input
def kruskal_menu():
    print("\n--- Kruskal's Algorithm ---")
    num_nodes = int(input("Enter the number of nodes: "))
    nodes = [input(f"Enter name for node {i+1}: ").strip() for i in range(num_nodes)]
    
    g = Graph(num_nodes)
    print("\nEnter the edges (e.g., A B 4 for edge A-B with weight 4):")
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter edge (u v weight): ").split()
        weight = int(weight)
        u_idx = nodes.index(u)
        v_idx = nodes.index(v)
        g.add_edge(u_idx, v_idx, weight)
    
    g.kruskal_mst()


# Main function
if __name__ == "__main__":
    menu()
