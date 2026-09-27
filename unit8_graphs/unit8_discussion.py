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
    if start not in graph:
        return []
    visited = {start}

    queue = deque([start])

    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal_order


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

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    campus_graph = {
        "Library": ["Science Hall", "Student Center"],
        "Science Hall": ["Library", "Gym", "Computer Lab"],
        "Student Center": ["Library", "Cafeteria"],
        "Gym": ["Science Hall", "Cafeteria"],
        "Computer Lab": ["Science Hall"],
        "Cafeteria": ["Student Center", "Gym"]
    }
    print("Campus graph:")
    for building, neighbors in campus_graph.items():
        print(f"{building}: {neighbors}")
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
    print("TODO: Perform and explain BFS traversal.")

    starting_building = "Library"

    traversal = bfs(campus_graph, starting_building)

    print(f"Starting building: {starting_building}")
    print(f"BFS traversal: {traversal}")

    campus_graph["Engineering Hall"] = ["Computer Lab"]
    campus_graph["Computer Lab"].append("Engineering Hall")

    new_traversal = bfs(campus_graph, starting_building)

    print(f"Updated graph: Added Engineering Hall")
    print(f"Updated BFS traversal: {new_traversal}")


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
    print("TODO: Demonstrate and explain edge cases.\n")

    print("Edge Case #1: Starting BFS from different node.")
    gym_traversal = bfs(campus_graph, "Gym")
    print(f"Starting from Gym: {gym_traversal}\n")

    print("Edge Case #2: Start BFS from node not in graph./n")
    missing_node = bfs(campus_graph, "Parking Lot")
    print(f"Starting from missing node Parking Lot: {missing_node}")


if __name__ == "__main__":
    main()