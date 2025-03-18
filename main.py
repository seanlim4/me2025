import timeit

dijSetup = """
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
"""

bfSetup = """
from algorithms import bruteforce
bf = bruteforce.Graph(5)

bf.add_vertex_data(0, 'A')
bf.add_vertex_data(1, 'B')
bf.add_vertex_data(2, 'C')
bf.add_vertex_data(3, 'D')
bf.add_vertex_data(4, 'E')

bf.add_edge(0, 1, 1)
bf.add_edge(0, 2, 2)
bf.add_edge(0, 4, 9)
bf.add_edge(1, 3, 5)
bf.add_edge(2, 3, 3)
bf.add_edge(3, 4, 2)
"""

bfExec = timeit.timeit(stmt="print(bf.bruteforce('A'))", setup=bfSetup, number=1000)
dijExec = timeit.timeit(stmt="print(dij.dijkstra('A'))", setup=dijSetup, number=1000)

print(f"bfExec runtime: {bfExec * 1000}ms")
print(f"dijExec runtime: {dijExec * 1000}ms")