import timeit
repetitions = 10000

dijSetup = """
from algorithms import dijkstra
dij = dijkstra.Graph(6)

dij.add_vertex_data(0, 'A')
dij.add_vertex_data(1, 'B')
dij.add_vertex_data(2, 'C')
dij.add_vertex_data(3, 'D')
dij.add_vertex_data(4, 'E')
dij.add_vertex_data(5, 'F')

dij.add_edge(0, 1, 1)
dij.add_edge(0, 2, 2)
dij.add_edge(0, 4, 9)
dij.add_edge(1, 3, 5)
dij.add_edge(2, 3, 3)
dij.add_edge(3, 4, 2)
dij.add_edge(1, 4, 8)
dij.add_edge(0, 5, 2)
dij.add_edge(4, 5, 10)
dij.add_edge(3, 5, 2)
"""

bfSetup = """
from algorithms import bruteforce
bf = bruteforce.Graph(6)

bf.add_vertex_data(0, 'A')
bf.add_vertex_data(1, 'B')
bf.add_vertex_data(2, 'C')
bf.add_vertex_data(3, 'D')
bf.add_vertex_data(4, 'E')
bf.add_vertex_data(5, 'F')

bf.add_edge(0, 1, 1)
bf.add_edge(0, 2, 2)
bf.add_edge(0, 4, 9)
bf.add_edge(1, 3, 5)
bf.add_edge(2, 3, 3)
bf.add_edge(3, 4, 2)
bf.add_edge(1, 4, 8)
bf.add_edge(0, 5, 2)
bf.add_edge(4, 5, 10)
bf.add_edge(3, 5, 2)
"""

aSSetup = """
from algorithms import astar
aS = astar.Graph(6)

aS.add_vertex_data(0, 'A')
aS.add_vertex_data(1, 'B')
aS.add_vertex_data(2, 'C')
aS.add_vertex_data(3, 'D')
aS.add_vertex_data(4, 'E')
aS.add_vertex_data(5, 'F')

aS.add_edge(0, 1, 1)
aS.add_edge(0, 2, 2)
aS.add_edge(0, 4, 9)
aS.add_edge(1, 3, 5)
aS.add_edge(2, 3, 3)
aS.add_edge(3, 4, 2)
aS.add_edge(1, 4, 8)
aS.add_edge(0, 5, 2)
aS.add_edge(4, 5, 10)
aS.add_edge(3, 5, 2)
"""

bfFile = open("data/bf.txt", 'a')
dijFile = open("data/dij.txt", 'a')
aSFile = open("data/as.txt", 'a')

for x in range(0, 100):
    bfExec = timeit.timeit(stmt="print(bf.bruteforce('A'))", setup=bfSetup, number=repetitions) * 1000 / repetitions
    dijExec = timeit.timeit(stmt="print(dij.dijkstra('A'))", setup=dijSetup, number=repetitions) * 1000 / repetitions
    aSExec = timeit.timeit(stmt="print(aS.astar('A', 'E'))", setup=aSSetup, number=repetitions) * 1000 / repetitions

    bfExec = round(bfExec, 3)
    dijExec = round(dijExec, 3)
    aSExec = round(aSExec, 3)

    print(f"bfExec runtime: {bfExec}ms")
    print(f"dijExec runtime: {dijExec}ms")
    print(f"aSExec runtime: {aSExec}ms")

    bfFile.write(f"{bfExec:.3f}\n")
    dijFile.write(f"{dijExec:.3f}\n")
    aSFile.write(f"{aSExec:.3f}\n")