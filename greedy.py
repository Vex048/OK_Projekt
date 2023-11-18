import sys
import math
import instances


def fromPointToPoint(curPoint):
    global points, visited
    if len(visited) == len(points):
        return
    minDistance = math.inf
    for point in points:
        if point == curPoint:
            print(curPoint[0], curPoint[1:])
            continue
        if point in visited:
            continue
        distance = math.sqrt(pow((point[1]-curPoint[1]), 2) +
                             pow((point[2]-curPoint[2]), 2))
        if distance < minDistance:
            minDistance = distance
            minPoint = point
    if minPoint not in visited:
        visited.append(minPoint)
    fromPointToPoint(minPoint)


# pointCount, points = instances.readFromFile(sys.argv[1])
pointCount, points = instances.randomInstance(29, 2500, 2500)
visited = [points[0]]


fromPointToPoint(points[0])
