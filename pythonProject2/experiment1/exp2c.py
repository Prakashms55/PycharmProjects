import heapq


def a_star(graph, start, goal, h):
    # Priority queue to store (cost, node) tuples
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Dictionaries to store the cost to reach each node and the path
    g_costs = {start: 0}
    came_from = {start: None}

    while open_list:
        # Get the node with the lowest cost
        current_cost, current_node = heapq.heappop(open_list)

        # If we have reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]  # Return reversed path

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            tentative_g_cost = g_costs[current_node] + weight

            # If this path to neighbor is better, record it
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + h(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None  # No path found


# Example usage:
# Define the graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}


# Define a simple heuristic function (e.g., straight-line distance)
def heuristic(node, goal):
    heuristics = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 4,
        'F': 0
    }
    return heuristics.get(node, float('inf'))



path = a_star(graph, 'A', 'F', heuristic)
print("Shortest path:", path)
