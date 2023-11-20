import sys
import math
import instances


def fromPointToPoint(curPoint):
    global points, visited, totalDistance
    if len(visited) == len(points):
        return
    minDistance = math.inf
    for point in points:
        if point == curPoint:
            print(curPoint[0], curPoint[1:], end='')
            continue
        if point in visited:
            continue
        distance = math.sqrt(pow((point[1]-curPoint[1]), 2) +
                             pow((point[2]-curPoint[2]), 2))
        totalDistance += distance
        if distance < minDistance:
            minDistance = distance
            minPoint = point
    if minPoint not in visited:
        visited.append(minPoint)
    print(f' Distance: {round(minDistance, 3)}')
    fromPointToPoint(minPoint)


if (len(sys.argv) == 2):
    pointCount, points = instances.readFromFile(sys.argv[1])
else:
    pointCount, points = instances.randomInstance(29, 2500, 2500)
visited = [points[0]]
totalDistance = 0


fromPointToPoint(points[0])
print(f'Total distance: {round(totalDistance, 3)}')
