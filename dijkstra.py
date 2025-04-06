def dijkstra(graph, start_province, end_province, optimization_criterion):
    # Convert province names to indices
    start_idx = graph.vertex_index.get(start_province)
    end_idx = graph.vertex_index.get(end_province)

    # Manual priority queue (list that we'll keep sorted)
    priority_queue = []
    priority_queue.append((0, start_idx, [start_idx]))
    
    visited = set()

    while priority_queue:
        # Manually find and remove the item with minimum cost
        min_index = 0
        for i in range(1, len(priority_queue)):
            if priority_queue[i][0] < priority_queue[min_index][0]:
                min_index = i
        path_cost, current, path = priority_queue.pop(min_index)
        
        if current == end_idx:
            return [graph.vertex_data[i] for i in path], path_cost
            
        if current in visited:
            continue
            
        visited.add(current)
        
        for neighbor in range(graph.size):
            edge = graph.adj_matrix[current][neighbor]
            if edge is not None:
                new_cost = path_cost + edge[optimization_criterion]
                new_path = path + [neighbor]
                
                # Insert into queue (sort it later)
                priority_queue.append((new_cost, neighbor, new_path))
        
        # Maintain queue order by sorting
        priority_queue.sort()

    return None