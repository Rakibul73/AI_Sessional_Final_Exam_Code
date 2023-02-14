nodes = ['A', 'B','C','F','O','P','R','S']
weightedEdges = [
    ['A','C',494],
    ['A','S',140],
    ['A','O',146],
    ['O','S',151],
    ['C','R',146],
    ['C','P',138],
    ['S','F',99],
    ['S','R',80],
    ['R','P',97],
    ['F','B',211],
    ['P','B',101]
]

initialState = 'A'
goalState = 'B'

goalPath = [initialState]
totalCost = []

n = initialState
while n != goalState:
    neighbours = [edge for edge in weightedEdges if edge[0] == n]
    minCost = [edge for edge in neighbours if edge[2] == min([edge[2] for edge in neighbours]) ][0]
    n = minCost[1]
    goalPath.append(n)
    totalCost.append(minCost[2])
    print(f"Next Node is {n} at min cost: {minCost[2]}")

print(f"{'-'*20}\nThe Goal Path is: {goalPath} \nWith Total Cost of {sum(totalCost)} \nHaving the cost of path {totalCost}")