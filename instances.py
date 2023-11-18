import random


def readFromFile(file):
    with open(file, 'r') as f:
        points = [[int(x) for x in line.split()] for line in f]
        return points[0][0], points[1:]


def randomInstance(instanceSize, boardX, boardY):
    points = []
    x = [int(x) for x in range(boardX-1)]
    y = [int(x) for x in range(boardY-1)]
    i = 1
    while len(points) != instanceSize:
        point = [i, random.choice(x), random.choice(y)]
        if point not in points:
            points.append(point)
            i += 1
    return instanceSize, points
