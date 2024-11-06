import heapq

# A* Algorithm implementation
def a_star(graph, start, end, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f_cost, node)
    g_cost = {start: 0}  # g_cost: cost to reach node
    f_cost = {start: heuristic[start]}  # f_cost: g_cost + heuristic
    came_from = {start: None}  # Came from path

    while open_list:
        current_priority, current_node = heapq.heappop(open_list)

        # If we've reached the end node, reconstruct the path
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], g_cost[end]  # Return path and total cost

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            tentative_g_cost = g_cost[current_node] + weight

            # If a better path to the neighbor is found
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = tentative_g_cost + heuristic[neighbor]
                came_from[neighbor] = current_node
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return None, float('inf')  # Return None if no path is found

# Function to input graph
def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for i in range(num_nodes):
        node = input(f"Enter the name of node {i+1}: ").strip().upper()  # Alphabet nodes (e.g., A, B, C)
        graph[node] = {}  # Initialize the node in the graph as an empty dictionary
        num_edges = int(input(f"Enter the number of edges for node {node}: "))
        
        for j in range(num_edges):
            u, v, weight = input(f"Enter edge {j+1} (format: node1 node2 weight): ").split()
            weight = int(weight)
            
            # Ensure that both u and v exist in the graph before adding edges
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            
            # Add the edge from u to v and v to u (undirected graph)
            graph[u][v] = weight
            graph[v][u] = weight
            
    return graph

# Function to input heuristic values for nodes
def input_heuristic(nodes):
    heuristic = {}
    print("Enter the heuristic value for each node:")
    
    for node in nodes:
        heuristic[node] = int(input(f"Heuristic value for {node}: "))
        
    return heuristic

# Main function
def main():
    graph = input_graph()  # Input the graph
    nodes = list(graph.keys())  # Convert dict_keys to list
    heuristic = input_heuristic(nodes)  # Input the heuristic values for each node
    
    # Input start and end nodes
    start = input("Enter the start node: ").strip().upper()
    end = input("Enter the end node: ").strip().upper()

    # Check if start and end nodes exist in the graph
    if start not in graph or end not in graph:
        print("Invalid start or end node.")
        return

    # Perform A* search
    path, cost = a_star(graph, start, end, heuristic)

    if path:
        print(f"Shortest path: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

