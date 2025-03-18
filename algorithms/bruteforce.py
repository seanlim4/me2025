class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bruteforce(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        
        def dfs(current, current_distance, visited):
            for neighbor in range(self.size):
                if self.adj_matrix[current][neighbor] != 0 and neighbor not in visited:
                    new_distance = current_distance + self.adj_matrix[current][neighbor]
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                    dfs(neighbor, new_distance, visited | {neighbor})
        
        dfs(start_vertex, 0, {start_vertex})
        return distances