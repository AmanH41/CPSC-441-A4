def dijkstra(graph, start_province, end_province, optimization_criterion): 
    # Convert province names to their corresponding indices
    start_index = graph.vertex_index.get(start_province)
    end_index = graph.vertex_index.get(end_province)
    
    # Handle case where provinces don't exist in the graph
    if start_index is None or end_index is None:
        return None, float('inf')
    
    # Import the heap queue module (done here to avoid global import)
    import heapq

    # Initialize the priority queue (min-heap) with the starting province:
    exploration_heap = []
    heapq.heappush(exploration_heap, (0, start_index, [start_index]))
    
    # Track visited provinces to avoid revisiting and cycles
    visited_provinces = set()
    
    while exploration_heap:
        # Get the path with current lowest cost from the heap
        path_cost, current_index, current_path = heapq.heappop(exploration_heap)
        
        # If we've reached the destination, return the optimal path
        if current_index == end_index:
            optimal_path = [graph.vertex_data[i] for i in current_path]
            return optimal_path, path_cost
        
        # Skip if we've already processed this province more efficiently
        if current_index in visited_provinces:
            continue
        
        # Mark current province as visited
        visited_provinces.add(current_index)
        
        # Examine all possible neighboring provinces
        for neighbor_index in range(graph.size):
            # Get connection details between current and neighbor province
            connection = graph.adj_matrix[current_index][neighbor_index]
            
            # Only proceed if a connection exists
            if connection is not None:
                # Calculate new cost by adding current connection's cost
                new_cost = path_cost + connection[optimization_criterion]
                
                # Create new path by extending with the neighbor
                new_path = current_path + [neighbor_index]
                
                # Add this new path to the exploration heap
                heapq.heappush(exploration_heap, (new_cost, neighbor_index, new_path))
    
    return None