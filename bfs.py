from collections import deque

def bfs(self, start_province, end_province, optimization_criterion):  
    # Convert province names to their corresponding indices
    start_index = self.vertex_index.get(start_province)
    end_index = self.vertex_index.get(end_province)
    
    # Check if provinces exist in the graph
    if start_index is None or end_index is None:
        return None, float('inf')
    
    # Initialize queue with starting point:
    exploration_queue = deque()
    exploration_queue.append((start_index, [start_index], 0))
    
    # List to store all valid paths that reach the destination
    successful_paths = []
    
    # PATH EXPLORATION  
    while exploration_queue:
        # Get the next path to explore from the queue
        current_vertex, current_path, path_cost = exploration_queue.popleft()
        
        # Check if we've reached our destination
        if current_vertex == end_index:
            successful_paths.append((current_path.copy(), path_cost))
            continue
        
        # Explore all neighboring provinces
        for neighbor_index in range(self.size):
            # Get connection details between current province and neighbor
            connection = self.adj_matrix[current_vertex][neighbor_index]
            
            # Only proceed if theres connection between vertex or we havent visited already visted neighbour in current path
            if connection is not None and neighbor_index not in current_path:
                # Calculate new cost by adding current connection's cost
                new_cost = path_cost + connection[optimization_criterion]
                
                # Create new path by adding the neighbor
                new_path = current_path + [neighbor_index]
                
                # Add this new path to the queue for further exploration
                exploration_queue.append((neighbor_index, new_path, new_cost))
    
    # Find the path with minimum cost according to our criterion
    best_path_indices, minimum_cost = min(successful_paths, key=lambda path_data: path_data[1])
    
    # Convert vertex indices back to province names for the final result
    best_path_names = [self.vertex_data[index] for index in best_path_indices]
    
    return best_path_names, minimum_cost