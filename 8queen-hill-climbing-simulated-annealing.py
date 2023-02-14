import random
import copy
import math
import time
import chess


def C2n(n):
    'returns C(2,n)'
    return n * (n-1) / 2


class CheckeredPageState:
    'defines a state. each column has only one queen in each state'

    def __init__(self, checkeredPage):
        self.checkeredPage = checkeredPage
        self.dimension = len(self.checkeredPage)
        self.setDic()
        self.setHeuristic()

    def setDic(self):
        'sets 3 dictionaries. for example: dicRows[i] = k means that the ith row has k queens in it. O(dimension^2)'
        dicRows = {}
        dicDiagonal1 = {}
        dicDiagonal2 = {}
        for i in range(self.dimension):
            dicRows[i] = 0
            for j in range(self.dimension):
                dicDiagonal1[i-j] = 0
                dicDiagonal2[i+j] = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.checkeredPage[i][j]:
                    dicRows[i] += 1
                    dicDiagonal1[i-j] += 1
                    dicDiagonal2[j+i] += 1
        self.dicRows = dicRows
        self.dicDiagonal1 = dicDiagonal1
        self.dicDiagonal2 = dicDiagonal2

    def setHeuristic(self):
        'sets heuristic of a state.heuristic of a state is the number of pairs of queens that are attacking each other. O(dimension) '
        h = 0
        for key in self.dicRows:
            if self.dicRows[key] > 1:
                h += C2n(self.dicRows[key])
        for key in self.dicDiagonal1:
            if self.dicDiagonal1[key] > 1:
                h += C2n(self.dicDiagonal1[key])
        for key in self.dicDiagonal2:
            if self.dicDiagonal2[key] > 1:
                h += C2n(self.dicDiagonal2[key])
        self.h = h

    def getRandomSteepestAscent(self):
        'between successors of a state which have the lowest heuristic, returns a random one. O(dimension^4)'
        neighbors = []
        huristic = float("inf")
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.checkeredPage[i][j] == 1:
                    ikeep = i
                    break
            for i in range(self.dimension):
                if self.checkeredPage[i][j] == 0:
                    newCheck = copy.deepcopy(self.checkeredPage)
                    newCheck[i][j] = 1
                    newCheck[ikeep][j] = 0
                    neighbor = CheckeredPageState(newCheck)
                    if neighbor.h < huristic:
                        neighbors[:] = []
                        huristic = neighbor.h
                    if neighbor.h == huristic:
                        neighbors.append(neighbor)
        return(random.choice(neighbors))

    def getFirstChoice(self):
        'randomly generates successors of a state until it finds a successor with heuristic lower than the hueristic of the current state'
        'otherwise it returns None'
        'O(dimension^4)'
        test = [[False for i in range(self.dimension)] for j in range(self.dimension)]
        while 1:
            i = random.randrange(0, self.dimension)
            j = random.randrange(0, self.dimension)
            test[i][j] = True
            newCheck = copy.deepcopy(self.checkeredPage)
            newCheck[i][j] = 1
            for k in range(self.dimension):
                if self.checkeredPage[k][j]:
                    ikeep = k
                    break
            newCheck[ikeep][j] = 0
            newCheck[i][j] = 1
            neighbor = CheckeredPageState(newCheck)
            if neighbor.h < self.h:
                return neighbor
            flag = True
            'checks if we have randomly generated all the successors. returns None if so'
            for x in test:
                for y in x:
                    if y is False:
                        flag = False
                        break
                if flag is False:
                    break
            if flag is True:
                return None

    def printPage(self):
        'prints the checkered page of the current state O(n^2)'
        for xs in self.checkeredPage:
            print(" ".join(map(str, xs)))

    def getMove(self, neighbor):
        'prints the move from the current state to the given neighbor state O(dimension^2)'
        test = False
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.checkeredPage[i][j] != neighbor.checkeredPage[i][j]:
                    if self.checkeredPage[i][j] == 1:
                        istart = i
                    else:
                        iend = i
                    if test is False:
                        test = True
                    else:
                        print("move in column "+ str(j+1) + " from row " + str(istart+1) + " to " + str(iend+1))
                        break

    def randomSuccessor(self):
        'returns a random successor of the current state O(dimension ^2)'
        j = random.randrange(0, self.dimension)
        while 1:
            i = random.randrange(0, self.dimension)
            if self.checkeredPage[i][j] != 1:
                break
        for k in range(self.dimension):
            if self.checkeredPage[k][j]:
                break
        newCheckeredPage = copy.deepcopy(self.checkeredPage)
        newCheckeredPage[i][j] = 1
        newCheckeredPage[k][j] = 0
        return CheckeredPageState(newCheckeredPage)


def HillCLimbingSteepestAscent(checkeredPageInitial):
    'gets the initial checkered page and performs the hill climbing algorithm steepest ascent variant'
    current = CheckeredPageState(checkeredPageInitial)
    print("start of hill climbing algorithm steepest ascent")
    while 1:
        print("current state checkered page:")
        current.printPage()
        print("current state h:", current.h)
        neighbor = current.getRandomSteepestAscent()
        if neighbor.h >= current.h:
            if current.h == 0:
                print("the hill climbing algorithm steepest ascent variant found a solution")
                return True, current
            else:
                print("the hill climbing algorithm steepest ascent variant got stuck in local minimum")
                return False, current
        current.getMove(neighbor)
        current = neighbor

def HillCLimbingFirstChoice(checkeredPageInitial):
    'gets the initial checkered page and performs the hill climbing algorithm first choice variant'
    current = CheckeredPageState(checkeredPageInitial)
    print("start of hill climbing algorithm first choice variant")
    while 1:
        print("current state checkered page:")
        current.printPage()
        print("current state h:", current.h)
        neighbor = current.getFirstChoice()
        if neighbor is None:
            if current.h == 0:
                print("the hill climbing algorithm first choice variant found a solution")
                return True, current
            else:
                print("the hill climbing algorithm first choice variant got stuck in local minimum")
                return False, current
        current.getMove(neighbor)
        current = neighbor


def getRandomCheckeredPage(dimension):
    'returns a random checkered page in which each column has exactly one queen in it'
    checkeredPage = [[0 for i in range(dimension)] for j in range(dimension)]
    randNumbers = random.sample(range(0, dimension), dimension)
    for j in range(dimension):
        checkeredPage[randNumbers[j]][j] = 1
    return checkeredPage

def HillClimbingRandomRestart(dimension):
    'gets the dimension of the page and performs the hill climbing algorithm with random restart'
    print("start of hill climbing algorithm with random restart")
    while 1:
        print("-----------------------------------")
        print("new start of hill climbing algorithm with random restart")
        checkeredPage = getRandomCheckeredPage(dimension)
        boolean, state = HillCLimbingSteepestAscent(checkeredPage)
        if boolean:
            print("the hill climbing algorithm with random restart ended")
            return state

def SimulatedAnnealing(checkeredPageInitial, T=4000, tChange=0.8):
    'gets the initial checkered page and performs the simulated annealing algorithm'
    current = CheckeredPageState(checkeredPageInitial)
    print("start of simulated annealing algorithm")
    while 1:
        print("current state checkered page:")
        current.printPage()
        print("current state h:", current.h)
        T *= tChange
        if T < 1:
            print("final state checkered page:")
            current.printPage()
            print("final state h:", current.h)
            if current.h == 0:
                print("the simulated annealing found a solution")
                return True, current
            else:
                print("the simulated annealing could not find the solution")
                return False, current
        next = current.randomSuccessor()
        deltaE = current.h - next.h
        if deltaE > 0:
            current.getMove(next)
            current = next
        else:
            rand = random.uniform(0, 1)
            probability = math.exp(deltaE / T)
            if rand <= probability:
                current.getMove(next)
                current = next



for i in range(1):
    print("------------------")
    randomCheck = getRandomCheckeredPage(8)
    print("new random check generated")
    startHillFirst = time.time()
    HillCLimbingFirstChoice(randomCheck)
    endHillFirst = time.time()
    print("------------------")
    HillCLimbingSteepestAscent(randomCheck)
    endHillSteep = time.time()
    print("------------------")
    # HillClimbingRandomRestart(8)
    endHillRandom = time.time()
    print("------------------")
    SimulatedAnnealing(randomCheck)
    endSim = time.time()
    print("run time of hill climbing first choice", endHillFirst - startHillFirst)
    print("run time of hill climbing steepest ascent", endHillSteep - endHillFirst)
    print("run time of hill climbing random restart", endHillRandom - endHillSteep)
    print("run time of simulated annealing", endSim - endHillSteep)


