import random
import sys
import math
import instances
import greedy


class Individual(object):  # Klasa osobników

    def __init__(self, order):
        self.order = order
        self.distance = self.calDistance()

    @staticmethod
    def mate(parent1, parent2):
        geneA = random.randint(0, pointCount-1)
        geneB = random.randint(0, pointCount-1)
        start = min(geneA, geneB)
        end = max(start+1, geneA, geneB)

        tmp = parent1[start:end]
        remaining = [x for x in parent2 if x not in tmp]
        # remaining = []
        # for x in parent2:
        #     if x not in tmp:
        #         remaining.append(x)
        res = remaining[:start] + tmp + remaining[start:]

        return res

    def mutate(self):
        pass

    def calDistance(self):
        totalDistance = 0
        startPoint = self.order[0]
        for endPoint in self.order[1:]:
            distance = math.sqrt(
                pow((endPoint[1]-startPoint[1]), 2) + pow((endPoint[2]-startPoint[2]), 2))
            totalDistance += distance
            startPoint = endPoint
        return totalDistance


def greedyOrder(points, start):
    return greedy.greedyPathStart(points, start)


def randomOrder(size, boardX, boardY):
    ord = [[i, random.randint(0, boardX), random.randint(
        0, boardY)] for i in range(1, size+1)]
    # ord = []
    # for i in range(1, size+1):
    #     ord.append([i, random.randint(0, boardX), random.randint(0, boardY)])
    random.shuffle(ord)
    ord.append(ord[0])
    return ord


def main():
    global pointCount

    if (len(sys.argv) == 2):
        pointCount, points = instances.readFromFile(f'tests/{sys.argv[1]}')
        boardX = max([point[1] for point in points])
        boardY = max([point[2] for point in points])
    else:
        pointCount, points = instances.randomInstance(
            29, boardX := 2500, boardY := 2500)

    POPULATION_SIZE = 100
    generation = 1
    population = []

    for i in range(pointCount):
        population.append(Individual(greedyOrder(points, i)))

    for _ in range(POPULATION_SIZE-pointCount):
        population.append(Individual(randomOrder(pointCount, boardX, boardY)))

    population.sort(key=lambda x: x.distance)

    # for ex in population:
    #     print([x[0] for x in ex.order], end=" ")
    #     print(ex.distance)

    for _ in range(100):
        newPopulation = []
        best = int((10*POPULATION_SIZE)/100)
        newPopulation.extend(population[:best])

        population = newPopulation
        generation += 1


if __name__ == "__main__":
    main()
