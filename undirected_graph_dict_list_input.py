# UNDIRECTED GRAPH

'''
graph = {
  '5' : ['3', '7'],
  '3' : ['2', '5'],
  '7' : ['8', '5'],
  '2' : ['3'],
  '8' : ['7']
}

'''

'''
V E
FOR EVERY EDGE
U V
4 4

5 3
5 7
3 2
7 8

'''
from collections import defaultdict
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)
for v in graph:
    print(v,graph[v])