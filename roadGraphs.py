import csv
import sklearn
import pandas as pd
import collections
import os
import sys
import numpy as np
import scipy as sp
from scipy.io import loadmat,savemat
import collections
import itertools
import copy


import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

SIZE=10

adj_array=np.zeros(())

#class stack:
    
    #def __init__(self):
        #"""Initializes this digraph."""
        #self.nodes = set()
        #self.edges = 0


    
    #def peek(self):     
        #return True      

    #def isFull(self):     
        #return True  
    
    #def isEmtpy(self):     
        #return True      
    
    

class roadGraph:
    """This class implements a directed, weighted graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph.
           Choose a set as this will auto store n unordered list of unique elements (towns)        
        """
        self.nodes = set()
        self.edges = 0
        self.children={}
        self.parents={}
        
        
        self.adjMat=np.zeros((127,127))
    
    def clear(self):
        """Clers up  this digraph.
           Choose a set as this will auto store n unordered list of unique elements (towns)        
        """
        self.nodes = set()
        self.edges = 0
        self.children={}
        self.parents={}
        
        
        self.adjMat=np.zeros((127,127))        
   
       
    ## load up 
    def loadData(self):    
        self.clear()
        
        argv=sys.argv  
        num_pairs=len(argv)
        
        #argvLst=list(argv[1:])
        
        for indx,val in enumerate(argv[1:]):
            
            node1=val[0]
            node2=val[1]
            dist=int(val[2])
        
            self.add_node(node1)
            self.add_node(node2)
            
            self.add_edge(node1,node2,dist)
            self.adjMat[ord(node1)][ord(node2)]=1 
                 

    def add_node(self, node):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""
        if node in self.nodes:
            return

        self.nodes.add(node)
        self.children[node] = dict()
        self.parents[node] = dict()

    def add_edge(self, tail, head, dist):
        """Creates a directed edge pointing from 'tail' to 'head' and assigns 'dist' as its weight."""
        if tail not in self.nodes:
            self.add_node(tail)

        if head not in self.nodes:
            self.add_node(head)

        self.children[tail][head] = dist
        self.parents[head][tail] = dist
        self.edges += 1
        
    def display(self):
        
        #for item in enumerate(self.nodes):
        #    print(item + " -> ")   


        for item in enumerate(self.nodes):
            print(str(item[1]) + " -> ") 
            for kids in self.children[item[1]]:
        
                print(str(kids))            
            
        
        return True
        
    def get_dist_route(*args, end):
        
townLst=[]
for towns in args[1][1:]:
    townLst.append(towns)

for index,town in enumerate(townLst):
    #check node exists:
    
    numeric_val1=ord(town[0])
    numeric_val2=ord(town[1])
    if not( town in self) or (self.adjMat[numeric_val1][numeric_val2] != 1) :
        
        print("NO SUCH Node \n")   
        next_index=index+1                   
    
    else:
        
        nunny=-1

return True    
    
    def get_num_routes(self, tail, head, weight):
        
        return True  
    
    def shortest_route(self, tail, head, weight):
        
        return True
    
    def does_route_exist(self, tail, head, weight):
        
        return True    
    
    def num_stops_in_route(self, tail, head, weight):
        
        return True  
    

if __name__ == "__main__":
    #roadGraphs.run()


    town_graph = roadGraph()
    
    town_graph.loadData()
    
    
    town_graph.display()
    
    
    
    argv=sys.argv
        
    town_graph.get_dist_route(argv,end=1)    
    
    check=-1