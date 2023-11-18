import random


def readFromFile(file):
    with open(file, 'r') as f:
        edges = [[int(x) for x in line.split()] for line in f]
        return edges[0][0], edges[1:]


def randomInstance(instanceSize, boardX, boardY):
    edges = []
    x = [int(x) for x in range(boardX)]
    y = [int(x) for x in range(boardY)]
    i = 0
    while len(edges) != instanceSize:
        point = [i, random.choice(x), random.choice(y)]
        if point not in edges:
            edges.append(point)
            i += 1
    return instanceSize, edges
