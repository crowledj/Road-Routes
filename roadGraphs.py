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

class stack:
    
    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.edges = 0

    def pop(self):
        return True
     
    def push(self):     
        return True
    
    def peek(self):     
        return True      

    def isFull(self):     
        return True  
    
    def isEmtpy(self):     
        return True      
    
    

class roadGraph:
    """This class implements a directed, weighted graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.edges = 0
        

    def add_node(self, node):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""
        if node in self.nodes:
            return

        self.nodes.add(node)
        self.children[node] = dict()
        self.parents[node] = dict()

    def add_edge(self, tail, head, weight):
        """Creates a directed edge pointing from 'tail' to 'head' and assigns 'weight' as its weight."""
        if tail not in self.nodes:
            self.add_node(tail)

        if head not in self.nodes:
            self.add_node(head)

        self.children[tail][head] = weight
        #self.parents[head][tail] = weight
        self.edges += 1
        
    def display(self, tail, head, weight):
        
        return True
        
    def get_dist_route(self, start, end, weight):
        
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
