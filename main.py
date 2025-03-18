from algorithms import dijkstra

dij = dijkstra.Graph(5)

dij.add_vertex_data(0, 'A')
dij.add_vertex_data(1, 'B')
dij.add_vertex_data(2, 'C')
dij.add_vertex_data(3, 'D')
dij.add_vertex_data(4, 'E')

dij.add_edge(0, 1, 1)
dij.add_edge(0, 2, 2)
dij.add_edge(0, 4, 9)
dij.add_edge(1, 3, 5)
dij.add_edge(2, 3, 3)
dij.add_edge(3, 4, 2)

distances = dij.dijkstra('A')
print(distances)