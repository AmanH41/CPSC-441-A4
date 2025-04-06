class Graph:
    def __init__(self, vertices):
        self.size = len(vertices)
        self.vertex_data = vertices
        self.vertex_index = {v: i for i, v in enumerate(vertices)}
        self.adj_matrix = [[None for _ in range(self.size)] for _ in range(self.size)]

    def add_edge(self, u, v, hops, distance, time, dementors):
        if u in self.vertex_index and v in self.vertex_index:
            u_idx = self.vertex_index[u]
            v_idx = self.vertex_index[v]
            self.adj_matrix[u_idx][v_idx] = {
                'hops': hops,
                'distance': distance,
                'time': time,
                'dementors': dementors
            }
        
        return None        
