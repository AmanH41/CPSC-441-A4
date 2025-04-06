def dijkstra(graph, start, end, criterion):

    # Convert province names to indices
    start_idx = graph.vertex_index.get(start)
    end_idx = graph.vertex_index.get(end)
    if start_idx is None or end_idx is None:
        return None, float('inf')

    import heapq
    heap = [(0, start_idx, [start_idx])]  # (total_cost, current_vertex, path)
    visited = set()

    while heap:
        current_cost, current, path = heapq.heappop(heap)
        
        if current == end_idx:
            return [graph.vertex_data[i] for i in path], current_cost
            
        if current in visited:
            continue
            
        visited.add(current)
        
        for neighbor in range(graph.size):
            edge = graph.adj_matrix[current][neighbor]
            if edge is not None:
                new_cost = current_cost + edge[criterion]
                heapq.heappush(heap, (new_cost, neighbor, path + [neighbor]))
    
    return None