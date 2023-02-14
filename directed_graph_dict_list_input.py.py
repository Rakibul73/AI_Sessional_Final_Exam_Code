# DIRECTED GRAPH

'''
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

'''
'''
V E
FOR EVERY EDGE
U V
6 6

5 3
5 7
3 2
3 4
7 8
4 8

'''
from collections import defaultdict
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    
for v in graph:
    print(v,graph[v])