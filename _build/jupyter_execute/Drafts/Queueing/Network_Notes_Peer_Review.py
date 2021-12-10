#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/dhirajbbasnet/Operations_Research/blob/main/Network_Notes_Peer_Review.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ##Network Draft Peer review by Queueing Theory Group 

# In[3]:


#Question 2 solution

#Shortest path problem solving using python...

import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]

    def printSolution(self, dist):
        print ("The shortest path from A to F is:- ")
        print(dist[self.V-1])

    #A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree

    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize


        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

 # Funtion that implements Dijkstra's single source
 # shortest path algorithm for a graph represented
 # using adjacency matrix representation

 # Implementation
    def dijkstra(self, src):
    
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
    
        for cout in range(self.V):

            x = self.minDistance(dist, sptSet)

            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

# Driver program
g = Graph(6)
g.graph = [[0, 13, 13, 11, 7, 0],
           [13, 0, 0, 0, 1, 0],
           [13, 0, 0, 0, 0, 6],
           [11, 0, 0, 0, 0, 2],
           [7, 1, 0, 0, 0, 4],
           [0, 0, 6, 2, 4, 0]]

g.dijkstra(0);


# In[1]:


#Question 3 Solution

#Shortest path problem solving using python...

import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]

    def printSolution(self, dist):
        print ("The shortest path from A to F is:- ")
        print(dist[self.V-1])

    #A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree

    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize


        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

 # Funtion that implements Dijkstra's single source
 # shortest path algorithm for a graph represented
 # using adjacency matrix representation

 # Implementation
    def dijkstra(self, src):
    
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
    
        for cout in range(self.V):

            x = self.minDistance(dist, sptSet)

            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

# Driver program
g = Graph(5)
g.graph = [[0,13,13,7,0],
           [13,0,0,1,6],
           [13,0,0,6,0],
           [7,1,6,0,4],
           [0,6,0,4,0]
           ];

g.dijkstra(0);


# In[ ]:



#Question 4 Solution
#Solving the above Question in example 2 to find maximal flow using python
#We took the codes as references from different python language sources and encoded in here.

class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
          
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                     
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        
        return False
             
     
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        while self.BFS(source, sink, parent) :
 
        
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
graph = [[0, 10, 10, 0 ,0],
         [0, 0, 2, 4, 0],
         [0, 0, 0, 10, 10],
         [0, 0, 0, 0, 10],
         [0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 4
  
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))


# Queries/Concerns about the Draft
# 
# 1. What does 0/9 mean on the graph max flow? 
# 2. How did you calculate the bottleneck capacity on example 2?
# 3. How did you calculate the maximal flow by hand?
# 4. It would be easier to have the accompanying graph for the solution in the first python example. (Shortest Path)
# 
