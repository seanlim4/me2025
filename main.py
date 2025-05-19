import timeit
repetitions = 10000

with open("bruteforce.txt", 'r') as a:
    bfSetup = a.read()
with open("dijkstra.txt", 'r') as b:
    dijSetup = b.read()
with open("astar.txt", 'r') as c:
    aSSetup = c.read()

bfFile = open("data/bf.txt", 'a')
dijFile = open("data/dij.txt", 'a')
aSFile = open("data/as.txt", 'a')

for x in range(0, 100):
    bfExec = timeit.timeit(stmt="print(bf.bruteforce('Tiong Bahru'))", setup=bfSetup, number=repetitions) * 1000 / repetitions
    dijExec = timeit.timeit(stmt="print(dij.dijkstra('Tiong Bahru'))", setup=dijSetup, number=repetitions) * 1000 / repetitions
    aSExec = timeit.timeit(stmt="print(aS.astar('Tiong Bahru', 'Changi Airport'))", setup=aSSetup, number=repetitions) * 1000 / repetitions

    bfExec = round(bfExec, 3)
    dijExec = round(dijExec, 3)
    aSExec = round(aSExec, 3)

    print(f"bfExec runtime: {bfExec}ms")
    print(f"dijExec runtime: {dijExec}ms")
    print(f"aSExec runtime: {aSExec}ms")

    bfFile.write(f"{bfExec:.3f}\n")
    dijFile.write(f"{dijExec:.3f}\n")
    aSFile.write(f"{aSExec:.3f}\n")