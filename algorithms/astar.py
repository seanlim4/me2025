import heapq

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.heuristics = [0] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def set_heuristic(self, vertex, heuristic_value):
        if 0 <= vertex < self.size:
            self.heuristics[vertex] = heuristic_value

    def astar(self, start_vertex_data, goal_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        goal_vertex = self.vertex_data.index(goal_vertex_data)
        
        open_set = []
        heapq.heappush(open_set, (0, start_vertex))
        
        came_from = {}
        g_score = {i: float('inf') for i in range(self.size)}
        g_score[start_vertex] = 0
        
        f_score = {i: float('inf') for i in range(self.size)}
        f_score[start_vertex] = self.heuristics[start_vertex]
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == goal_vertex:
                return g_score[goal_vertex]
            
            for neighbor in range(self.size):
                if self.adj_matrix[current][neighbor] != 0:
                    tentative_g_score = g_score[current] + self.adj_matrix[current][neighbor]
                    if tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + self.heuristics[neighbor]
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return float('inf')