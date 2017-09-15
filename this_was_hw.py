# -*- coding: utf-8 -*-
"""

"""
from SlideProblem import *

class Searches:    
    
    def graphBFS(self,problem):
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        print("I am an empty shell of a function.")        


    def idDFS(self,problem):
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        print("Please Implement me!")
        
if __name__ == '__main__':

    import time

    search=Searches()
    
    ''' Set up the search problem '''
    p=problem()
    s=state()
   
    p.goalState=state(s)
    
    p.apply('R',s)
    p.apply('R',s)
    p.apply('D',s)
    p.apply('D',s)
    p.apply('L',s)
    
    p.initialState=state(s)
    print(p.initialState)
    
    ''' 
    The sultion, should basically be the reverse order
    of backward moves above: RUULL
    '''
    
    print('=== Bfs  ===')
    startTime=time.clock()
    node.nodeCount=0
    
    res=search.graphBFS(p)
    print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
 
    print('=== ID-Depth Limited Search ===')
    startTime=time.clock()
    node.nodeCount=0

    res=search.idDFS(p)
    print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
 
      