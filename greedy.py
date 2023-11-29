from copy import deepcopy
import sys
import math
import instances

sys.setrecursionlimit(1000000)


def greedyPathStart(points, startIndex):
    global pointList, startPoint, visited, pointCount, path

    pointList = deepcopy(points)
    startPoint = pointList[startIndex]
    visited = [startPoint]
    pointCount = len(pointList)
    path = []
    greedyPathGen(startPoint)
    return path


def greedyPathGen(curPoint):
    path.append(curPoint)
    if len(visited) == pointCount:
        path.append(startPoint)
        return
    minDistance = math.inf
    for point in pointList:
        if point == curPoint:
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
    greedyPathGen(minPoint)


def fromPointToPoint(curPoint):
    print(curPoint[0], curPoint[1:])
    global totalDistance
    if len(visited) == pointCount:
        dist = math.sqrt(pow((startPoint[1]-curPoint[1]), 2) +
                         pow((startPoint[2]-curPoint[2]), 2))
        totalDistance += dist
        print(f"Distance to {startPoint[0]}: {round(dist, 3)}")
        print(startPoint[0], startPoint[1:])
        return
    minDistance = math.inf
    for point in points:
        if point == curPoint:
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
    totalDistance += minDistance
    print(f"Distance to {minPoint[0]}: {round(minDistance, 3)}")
    fromPointToPoint(minPoint)


def main():
    global pointCount, points, visited, startPoint, totalDistance
    if (len(sys.argv) == 2):
        pointCount, points = instances.readFromFile(f'tests/{sys.argv[1]}')
    else:
        pointCount, points = instances.randomInstance(29, 2500, 2500)
    visited = [startPoint := points[0]]
    totalDistance = 0

    fromPointToPoint(points[0])
    print(f'Total distance: {round(totalDistance, 3)}')


if __name__ == "__main__":
    main()
