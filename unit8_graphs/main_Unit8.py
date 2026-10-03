"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    #Return empty list if the starting location doesn't exist.
    if start not in graph:
        return []
    #Will keep track of locations the delivery driver has visited.
    visited = []

    #A queue is used to visit locations in the order they are found.
    queue = deque([start])

    while queue:
        #remove the first location from queue.
        current = queue.popleft()

        if current not in visited:
            visited.append(current)

            #Add neighboring locations to the queue so they can be visited next.
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    #BFS visits nearby locations level by level.
    #DFS would follow one route as far as possible before going back.
    return visited




def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    #Each node represents a delivery location.
    #Each edge will represent a road connecting two locations.
    graph = { "Warehouse": ["Red House", "Blue House"],
              "Red House":["Warehouse","Green House", "Yellow House"],
              "Blue House": ["Warehouse","Purple House"],
              "Green House": ["Red House"],
              "Yellow House": ["Red House"],
              "Purple House": ["Blue House"]}

    print("\n=== GRAPH STRUCTURE ===")

    #Display each location and its connections.
    for location, neighbor in graph.items():
        print(location, "->", neighbor)


    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.



    print("\n=== BFS TRAVERSAL ===")

    #The delivery driver starts at the Warehouse.
    #BFS Visits the closest connected locations first.
    start = "Warehouse"
    order = bfs(graph, start)

    print("Starting location:", start)
    print("Delivery order:", order)

    #Add a new delivery location connected to Purple House
    graph["Purple House"].append("Orange House")
    graph["Orange House"] = ["Purple House"]

    #Run BFS again to show the updated traversal.
    updated_order = bfs(graph, start)
    print("Updated delivery order:", updated_order)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    #Edge Case 1: Start from a different delivery location.
    print("Starting from Blue House:")
    print(bfs(graph,"Blue House"))

    #Edge Case 2: Start from a location that doesn't exist.
    #The program safely returns an empty list.
    print("Starting from Gray House:")
    print(bfs(graph,"Gray House"))



if __name__ == "__main__":
    main()