# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:16:21 2020

@author: Venni
"""

# BREADTH FIRST SEARCH
def bfs(graph, root):
    '''
    Breadth First Search
    
    Needs Collections model to be imported
    
    Parameters
    ----------
    graph : a set
        
    root : an integer     
        
        Starting Position of the Search
    
    Returns
    -------
    a set of distances from the starting position to the respective nodes
    '''
    distances = {}
    distances[root] = 0
    
    q = deque([root])
    
    while q:
        current = q.popleft()
        for neighbour in graph[current]:
            if neighbour not in distances:
                q[neighbour] = q[current] + 1
                q.append(neighbour)
    return distances
        