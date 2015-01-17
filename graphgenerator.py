# Program used to generate randomized graphs.
# Will save a randomly generated graph of the type choses to graph.txt.
#
# The 4 different types of graphs are:
# 1. Unweighted, undirected graph
# 2. Unweighted, directed graph
# 3. Weighted, undirected graph
# 4. Weighted, directed graph
#
# The amount of nodes and type of graph is decided by keyboard input
# when running the program

import random

def uwud():
    file = open("graph.txt", "w")
    print "An unweighted, undirected graph  has been printed to graph.txt"
    graph = [[0 for x in range(size)] for x in range(size)]
    for x in range(size):
        for y in range(size):
            if x < y:
                graph[x][y] = random.randint(0, 1)
                graph[y][x] = graph[x][y]
    file.write("{{")
    file.write(('},\n{'.join([','.join(['{:1}'.format(item) for item in row]) 
      for row in graph])))
    file.write("}}")
    file.close()

def uwd():
    file = open("graph.txt", "w")
    print "An unweighted, directed graph has been printed to graph.txt"
    graph = [[0 for x in range(size)] for x in range(size)]
    for x in range(size):
        for y in range(size):
            if x != y:
                graph[x][y] = random.randint(0, 1)
    file.write("{{")
    file.write(('},\n{'.join([','.join(['{:1}'.format(item) for item in row]) 
      for row in graph])))
    file.write("}}")
    file.close()

def wud():
    maxweight = input("Max edge weight: ")
    file = open("graph.txt", "w")
    print "A weighted, undirected graph has been printed to graph.txt"
    graph = [[0 for x in range(size)] for x in range(size)]
    for x in range(size):
        for y in range(size):
            if x < y:
                graph[x][y] = random.randint(0, maxweight)
                graph[y][x] = graph[x][y]
    file.write("{{")
    file.write(('},\n{'.join([','.join(['{:1}'.format(item) for item in row]) 
      for row in graph])))
    file.write("}}")
    file.close()

def wd():
    maxweight = input("Max edge weight: ")
    file = open("graph.txt", "w")
    print "A weighted, directed graph has been printed to graph.txt"
    graph = [[random.randint(0, maxweight) for x in range(size)] for x in range(size)]
    for x in range(size):
        for y in range(size):
            if x != y:
                graph[x][y] = random.randint(0, maxweight)
    file.write("{{")
    file.write(('},\n{'.join([','.join(['{:1}'.format(item) for item in row]) 
      for row in graph])))
    file.write("}}")
    file.close()

# map the inputs to the function blocks
options = {1 : uwud,
           2 : uwd,
           3 : wud,
           4 : wd,
}

while True:
    size = input("Size of graph: ")
    if size > 0 and isinstance(size, int):
        break;
    else:
        print "Please insert a positive integer as size"

print "Choose graph type by entering the number corresponding to the graph type"
print "(1: Unweighted, undirected, 2: Unweighted, directed,"
print "3: Weighted, undirected, 4: Weighted, directed)"

type = input("Choice: ")
while True:
    try:
        options[type]()
        break
    except KeyError:
        print "Incorrect graph type. Please choose a number between 1 and 4"
        type = input("Choice:")