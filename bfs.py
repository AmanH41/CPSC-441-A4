def bfs(self, start_province, end_province, optimization_criterion):
    # Convert province names to their corresponding indices
    start_index = self.vertex_index.get(start_province)
    end_index = self.vertex_index.get(end_province)
    
    # Check if provinces exist in the graph
    if start_index is None or end_index is None:
        return None, float('inf')
    
    # Initialize queue using a list (instead of deque)
    exploration_queue = []
    exploration_queue.append((start_index, [start_index], 0))  # (vertex, path, cost)
    
    # List to store all valid paths that reach the destination
    successful_paths = []
    
    # PATH EXPLORATION
    while exploration_queue:
        # Simulate popleft() by popping from front (index 0)
        current_vertex, current_path, path_cost = exploration_queue.pop(0)
        
        # Check if we've reached our destination
        if current_vertex == end_index:
            successful_paths.append((current_path.copy(), path_cost))
            continue
        
        # Explore all neighboring provinces
        for neighbor_index in range(self.size):
            # Get connection details between current province and neighbor
            connection = self.adj_matrix[current_vertex][neighbor_index]
            
            # Only proceed if connection exists and neighbor not in current path
            if connection is not None and neighbor_index not in current_path:
                # Calculate new cost
                new_cost = path_cost + connection[optimization_criterion]
                
                # Create new path
                new_path = current_path + [neighbor_index]
                
                # Append to end of queue (FIFO behavior)
                exploration_queue.append((neighbor_index, new_path, new_cost))
    
    # If no paths found
    if not successful_paths:
        return None, float('inf')
    
    # Find the minimum cost path
    best_path_indices, minimum_cost = min(successful_paths, key=lambda x: x[1])
    
    # Convert indices back to province names
    best_path_names = [self.vertex_data[i] for i in best_path_indices]
    
    return best_path_names, minimum_cost