graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def DLS(start,goal,path,level):
  print('\nCurrent level-->',level)
  print('Goal node testing for',start)
  path.append(start)
  if start == goal:
    print("Goal test successful")
    return path
  print('Goal node testing failed')
  print('\nExpanding the current node',start)
  for child in graph[start]:
    if DLS(child,goal,path,level+1):
      return path
    path.pop()
  return False
  
  
  
start = 'A'
goal = input('Enter the goal node:-')

print()
path = list()
res = DLS(start,goal,path,0)
if(res):
    print("Path to goal node available")
    print("Path",path)
else:
    print("goal nai")
            