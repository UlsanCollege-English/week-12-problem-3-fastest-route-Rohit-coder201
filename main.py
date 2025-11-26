import heapq

def dijkstra_shortest_path(graph, start, goal):
    # If start or goal does not exist → return empty and None
    if start not in graph or goal not in graph:
        return ([], None)

    # If start == goal → cost = 0 and path is just [start]
    if start == goal:
        return ([start], 0)

    # Distance dictionary: store minimum cost to reach each node
    dist = {start: 0}
    # Parent map: to reconstruct the shortest path
    parent = {start: None}

    # Min-heap priority queue: (current_cost, node)
    heap = [(0, start)]

    while heap:
        current_cost, current = heapq.heappop(heap)

        # If we reached the goal → stop early
        if current == goal:
            break

        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            new_cost = current_cost + weight

            # If this path is shorter → update
            if neighbor not in dist or new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(heap, (new_cost, neighbor))

    # If goal was never reached → unreachable
    if goal not in dist:
        return ([], None)

    # Reconstruct path by walking parent pointers backwards
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return (path, dist[goal])


if __name__ == "__main__":
    sample_graph = {
        "K1": [("K2", 5), ("K3", 2)],
        "K2": [("K1", 5), ("K4", 4)],
        "K3": [("K1", 2), ("K4", 7)],
        "K4": [("K2", 4), ("K3", 7)],
    }
    p, c = dijkstra_shortest_path(sample_graph, "K1", "K4")
    print("Sample path from K1 to K4:", p, "cost:", c)
