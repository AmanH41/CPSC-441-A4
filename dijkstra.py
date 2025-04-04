def dijkstra(self, start_vertex_data):
    start_vertex = self.vertex_data.index(start_vertex_data)
    distances = [float('inf')] * self.size
    distances[start_vertex] = 0
    visited = [False] * self.size

    for _ in range(self.size):
        min_distance = float('inf')
        u = None
        for i in range(self.size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break

        visited[u] = True

        for v in range(self.size):
            if self.adj_matrix[u][v] != 0 and not visited[v]:
                alt = distances[u] + self.adj_matrix[u][v]
                if alt < distances[v]:
                    distances[v] = alt

    return distances

    def get_path_dijkstra(self, start, end, criterion):
        """
        Find the optimal path based on the criterion:
        - 'hops': BFS (fewest connections)
        - 'distance', 'time', 'dementors': Dijkstra's (minimize total weight)
        """
        if criterion not in ['hops', 'distance', 'time', 'dementors']:
            raise ValueError("Invalid criterion. Use 'hops', 'distance', 'time', or 'dementors'.")

        start_idx = self.vertex_index.get(start)
        end_idx = self.vertex_index.get(end)
        if start_idx is None or end_idx is None:
            return None

        if criterion == 'hops':
            return self._bfs_shortest_hops(start_idx, end_idx)
        else:
            return self._dijkstra(start_idx, end_idx, criterion)
