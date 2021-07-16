import math

def prims_algorithm(graph, start):
  ''' Prim's algorithm is very similar to Dijkstra’s algorithm,
  but produces a Minimum Spanning Tree (MST) instead of a shortest path.
  This MST represents the path between all the vertices with the least total distance used.
  It can be used for tasks such as designing roadways.
  Unlike Dijkstra’s algorithm, which can be used for both directed or undirected paths, 
  Prim's algorithm can only be used for undirected paths. 
  '''

  mst = {}  # a dictionary in the same format as graph that will store the final mst

  mstSet = []  # keep track of which vertices have already been added to the MST

  # each vertex has a key value. they will default to -1, representing INF
  # also keeping track of the vert that it came from
  key_values = {} 
  for vert in graph:
      key_values[vert] = (-1, None)  # tuple (val, source)
      mst[vert] = []  # also set up empty mst
  key_values[start] = (0, start)  # the starting vertex has a key value of 0

  # loop while mstSet doesn't contain all vertices
  while len(mstSet) < len(graph):
    # find the vert with the least key value NOT already in mstSet (if tie, choose either)
    vert = pick_smallest_key(key_values, mstSet)  # see helper func
    # add vert to mstSet
    mstSet.append(vert)
    # add the connections to the mst
    if vert != key_values[vert][1]: # skip redundant connectoins
      mst[vert].append((key_values[vert][1], key_values[vert][0]))
      mst[key_values[vert][1]].append((vert, key_values[vert][0]))
    # update the key values of adjacent verts
    for adj in graph[vert]:  # adj is tuple (location, distance)
      if adj[1] < key_values[adj[0]][0] or key_values[adj[0]][0] == -1:
        key_values[adj[0]] = (adj[1], vert)

  return(mst)

def pick_smallest_key(key_values, mstSet):
  '''Pick the vertex with the smallest key value (not -1 or in mstSet)'''
  print(key_values)
  print(mstSet)
  smallest = None
  for vert, val in key_values.items():
    if vert not in mstSet:  # otherwise already used
      if smallest is None:
        # first applicable vert, set smallest
        smallest = vert
      elif (val[0] <= key_values[smallest][0]) and (val[0] != -1):
        smallest = vert
  print(smallest)
  return smallest
  
