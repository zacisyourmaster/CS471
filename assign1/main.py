"""
For this problem, you are only allowed to use standard python libraries. 
You may not use third party libraries or call any shell/bash functions. 
You are given a list of tuples of the form (<float> x, <float> y, <float> r) (Let's call these c-tuples). 
Each c-tuple represents a circle on a rectangular coordinate space, 
with x and y being the coordinates of the center, and r being the radius. 
Assume that each c-tuple has a unique radius. 

Let a cluster of circles be a group of circles where each circle in the group overlaps with at least one other circle in that group. 
A path is formed between two circles when they overlap. Define a cluster as a group of n circles, 
where each circle is reachable from every other circle through the formed paths. 

Write a python script that does the following: 
Return True if the given circles form a cluster and return false if they don't form a cluster. 
"""
import math

class Node:
    def __init__(self, circle: tuple) -> None:
        self.circle = circle

class Graph:
    def __init__(self, size) -> None:
        self.nodes = []
        self.matrix = [[0] * size for _ in range(size)]

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, src, dst):
        self.matrix[src][dst] = 1
        self.matrix[dst][src] = 1

    def check_edge(self, src, dst) -> bool:
        return self.matrix[src][dst] == 1
    
    def dfs(self,start,visited:list):
        visited.append(start)
        
        for i in range(len(self.nodes)):
            if self.matrix[start][i]==1 and i not in visited:
                self.dfs(i,visited)
                
        return visited
    
    def is_cluster(self):
        visited=[]
        visited=self.dfs(0,visited)
        
        return len(visited)==len(self.nodes)

def overlap(c1,c2)->bool:
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist <= r1 + r2 and dist >= abs(r1 - r2)

if __name__ == "__main__":
    t1=[(1,3,.7),(2,3,.4),(3,3,.9)]
    t2=[(1.5,1.5,1.3),(4,4,0.7)]
    t3=[(.5,.5,.5),(1.5,1.5,1.1),(.7,.7,.4),(4,4,.7)]
    t4 = [(0, 0, 4), (-10, 0, 4)]
    tests=[t1,t2,t3,t4]
    for i,circles in enumerate(tests):
        print(f"Test Case {i+1}:")
        print(f"    Input:  {circles}")
        
        graph = Graph(len(circles))
        for i in range(len(circles)):
            graph.add_node(Node(circles[i]))

        for i in range(len(circles)):
            for j in range(i + 1, len(circles)):
                if overlap(circles[i], circles[j]):
                    graph.add_edge(i, j)

        output=graph.is_cluster()
        
        print(f"    Output: {output}\n")