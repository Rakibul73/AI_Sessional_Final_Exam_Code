graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] 
queue = []     

def bfs(visited, graph, node ):
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ")
    # if (m == goal):          
    #   print ("\nGoal Node " + goal + " Found\n")
    #   return
    

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
    


# goal = input('Enter the goal node:-')
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')    