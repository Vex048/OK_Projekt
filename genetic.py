from copy import deepcopy
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
        geneA = random.randint(1, pointCount-1)
        geneB = random.randint(1, pointCount-1)
        start = min(geneA, geneB)
        end = max(start+1, geneA, geneB)

        tmp = parent1[start:end]
        remaining = [x for x in parent2 if x not in tmp]
        # remaining = []
        # for x in parent2:
        #     if x not in tmp:
        #         remaining.append(x)
        res = remaining[:start] + tmp + remaining[start:]
        if len(res) != pointCount+1:
            res.append(res[0])
        return res

    def mutate(self):
        while True:
            geneA = random.randint(1, pointCount-1)
            geneB = random.randint(1, pointCount-1)
            if geneA != geneB:
                if geneA > geneB:
                    geneA, geneB = geneB, geneA
                oldDistance = self.distanceBetweenGenes(geneA-1, geneB+1)
                self.order[geneA], self.order[geneB] = self.order[geneB], self.order[geneA]
                newDistance = self.distanceBetweenGenes(geneA-1, geneB+1)
                self.distance -= oldDistance
                self.distance += newDistance
                return

    def calDistance(self):
        totalDistance = 0
        startPoint = self.order[0]
        for endPoint in self.order[1:]:
            distance = math.sqrt(
                pow((endPoint[1]-startPoint[1]), 2) + pow((endPoint[2]-startPoint[2]), 2))
            totalDistance += distance
            startPoint = endPoint
        return totalDistance

    def distanceBetweenGenes(self, geneA, geneB):
        totalDistance = 0
        startPoint = self.order[geneA]
        for endPoint in self.order[geneA+1:geneB+1]:
            distance = math.sqrt(
                pow((endPoint[1]-startPoint[1]), 2) + pow((endPoint[2]-startPoint[2]), 2))
            totalDistance += distance
            startPoint = endPoint
        return totalDistance


def greedyOrder(points, start):
    return greedy.greedyPathStart(points, start)


def randomOrder(points):
    ord = deepcopy(points)
    random.shuffle(ord)
    ord.append(ord[0])
    return ord


def main():
    global pointCount

    if (len(sys.argv) == 2):
        pointCount, points = instances.readFromFile(f"tests/{sys.argv[1]}.txt")
    else:
        pointCount, points = instances.randomInstance(29, 2500, 2500)

    POPULATION_SIZE = 10000
    s = int(POPULATION_SIZE/2)
    generation = 1
    population = []

    for i in range(pointCount):
        population.append(Individual(greedyOrder(points, i)))

    for _ in range(POPULATION_SIZE-pointCount):
        population.append(Individual(randomOrder(points)))

    # for _ in range(POPULATION_SIZE):
    #     population.append(Individual(randomOrder(points)))

    population.sort(key=lambda x: x.distance)

    print(f"Generation {generation}, distance {population[0].distance}")

    for _ in range(1000):
        generation += 1
        newPopulation = []
        best = int((10*POPULATION_SIZE)/100)
        newPopulation.extend(population[:best])

        mate = int((80*POPULATION_SIZE)/100)
        for _ in range(mate):
            parent1 = random.choice(population[:s])
            parent2 = random.choice(population[:s])
            child = Individual.mate(parent1.order, parent2.order)
            newPopulation.append(Individual(child))

        mut = int((10*POPULATION_SIZE)/100)
        for _ in range(mut):
            x = deepcopy(random.choice(population[:s]))
            x.mutate()
            newPopulation.append(x)

        population = newPopulation
        population.sort(key=lambda x: x.distance)

        print(f"Generation {generation}, distance {population[0].distance}")


if __name__ == "__main__":
    main()
