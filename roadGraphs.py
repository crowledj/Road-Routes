import csv
import sklearn
import pandas as pd
import collections
import os
import sys
import numpy as np
import scipy as sp
from scipy.io import loadmat,savemat
import itertools
from itertools import permutations
import copy


## declaration if some utility functions :
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


def pairwise(lst):
    """ yield item i and item i+1 in lst. e.g.
        (lst[0], lst[1]), (lst[1], lst[2]), ..., (lst[-1], None)
    """
    if not lst: return

    for i in range(len(lst)-1):
        yield lst[i], lst[i+1]
    yield lst[-1], None    



class roadGraph:
    """This class implements a directed, weighted graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph.
           Choose a set as this will auto store n unordered list of unique elements (towns)        
        """
        self.clear()

    
    def clear(self):
        """Clers up  this digraph.
           Choose a set as this will auto store n unordered list of unique elements (towns)        
        """
        self.nodes =  collections.defaultdict(list)
        self.nodes_mapping =  collections.defaultdict(list)
        self.edges = 0
        #self.children_length={}
        self.parents_length = collections.defaultdict(lambda : collections.defaultdict(int))  
                     

       
    ## load up 
    def loadData(self):    
        
        argv=sys.argv  
        num_pairs=len(argv)
               
        for indx,val in enumerate(argv[1:]):
            
            node1=val[0]
            node2=val[1]
            dist=int(val[2])
        
            self.add_node_pairs(node1,node2)         
            self.add_edge(node1,node2,dist)
        
        for indx,vals in enumerate(self.nodes):
            self.nodes_mapping[vals]=indx
            
            
                 

    def add_node_pairs(self, node_a,node_b):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""
        
        if node_b is not None : 
            self.nodes[node_a].append(node_b)


    def add_edge(self, head, tail, dist):
        """Creates a directed edge pointing from 'tail' to 'head' and assigns 'dist' as its weight."""
        if tail not in self.nodes:
            self.add_node_pairs(head,None)

        if head not in self.nodes:
            self.add_node_pairs(head,tail)


        self.parents_length[head][tail]=dist
        self.edges += 1

    def printAllPathsUtil(self, start, end, visited, path):
        
        global paths_list
        global dist_list
        global num_town_list


        # Mark the current node as visited and store in path
        #also can't have a town link to itself but can return to a given town:        
        visited[self.nodes_mapping[start]]= True
        path.append(start)

        # If current vertex is same as destination, then print
        # current path[]
       
        if start == end and len(path) >=2 : #and iter_num != 0:
            num_towns=len(path)
            route_dist=0
            for twn in range(len(path)-1):
                route_dist+=self.parents_length[path[twn]][path[twn+1]]
            print(str(path) + " --  num_towns = " + str(num_towns) + " --  length trip =  "  + str(route_dist) + "\n")
            
            path_copy=copy.copy(path)
            paths_list.append(path_copy)
            dist_list.append(route_dist)
            num_town_list.append(num_towns)
            
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            for i in self.nodes[start]:
                if visited[self.nodes_mapping[i]]==False :

                    self.printAllPathsUtil(i, end, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[self.nodes_mapping[start]]= False        
    
            
    

    # visits all the nodes of a graph (connected component) using BFS
    def bfs_connected_component(self, start,end,length):
        #
        path = []
                
        global paths_list
        global dist_list
        global num_town_list 
        
        global glob_iter
        
        #path[0]=start
        # keep track of nodes to be checked
        queue = [start]
    
        # keep looping until there are nodes still to be checked
        while queue:
            glob_iter+=1
            # pop shallowest node (first node) from queue
            #path=queue[-1]
            node = queue.pop(0)
            #if node not in explored:
                # add node to list of checked nodes
                
            path.append(node)
            last=path[-1]
            if (last == end and len(path) < 10):
                print(path)
                print("\n")
                #break
            neighbours = self.nodes[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                
                if (queue):
                    if (neighbour != queue[-1]):
                        queue.append(neighbour)
                    else:
                        continue
                else:
                    queue.append(neighbour)

    
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
    argv=sys.argv
        

    visited =[False]*len(town_graph.nodes)

    # Create an array to store paths
    
    path_local = []    
    paths_list=[]
    dist_list=[]
    num_town_list=[]          
    cycle=False
    glob_iter=0
    
    town_graph.printAllPathsUtil('A', 'C',visited,path_local)      
    
    
    

    # get all existing paths from town 'a' -> ? -? -> town 'b'
    # use this list to answer the Qs.
    
    #i.e. do for all trips starting with town 'A', ending in town 'C' to answer Q 1,3,7 , 8
    
    # ... and   " " " "  ..town 'A'  " " "  "  .. ending in town 'D' for Qs  2,4,5
    
    # Qs 6 and 9 are answered by setting start town to end at same place... 
    
    ###So for town 'A', ending in town 'C' to answer Q 1,3,7 , 8
    ##print("calculating trip of all routes between town " + " " + 'A'  + " " + 'C' + ".... : \n\n")
    ##1. The distance of the route A-B-C.
    correct_dist=0
    correct_result=[index for index,l in enumerate(paths_list) if len(l) == 3 and l[1] == 'B']
    if not correct_result:
        print("NO SUCH ROUTE ! \n")
    else:      
        if len(correct_result)==1:
            correct_dist=dist_list[int(correct_result[0])]
    
    
    print("Q 1 -- answer =  " + str(correct_dist))
    
    ##3. The distance of the route A-D-C.
    correct_result=[index for index,l in enumerate(paths_list) if len(l) == 3 and l[1] == 'D']
    if not correct_result:
        print("NO SUCH ROUTE ! \n")
    else:      
        if len(correct_result)==1:
            correct_dist=dist_list[int(correct_result[0])]
    
    
    print("Q 3 -- answer =  " + str(correct_dist))    
    


    
    ##7. The number of trips starting at A and ending at C with exactly 4 stops.
    ##In the sample data below, there are three such trips: A to C (via B,C,D); A
    ##to C (via D,C,D); and A to C (via D,E,B).
    
    
    
    
    ##8. The length of the shortest route (in terms of distance to travel) from A
    ##to C.
    
    minDist=sys.maxsize
    
    for index,dists in enumerate(dist_list):
        
        if dists < minDist:
            minDist=dists
            minIndex=index
     
    print("Q 8 -- answer =  " + str(minDist))                
    
    
    
    
    ##***** FOR Q 2 : *****    

    ##RESET a-C route values and re-do for A->D:
    paths_list=[]
    dist_list=[]
    num_town_list=[]
    visited =[False]*len(town_graph.nodes)
    # Call the recursive helper function to print all paths
    town_graph.printAllPathsUtil('A', 'D',visited, path_local)      

    
    
    #2. The distance of the route A-D
    
    correct_result=[index for index,l in enumerate(paths_list) if len(l) == 2 and l[1] == 'D']
    if not correct_result:
        print("NO SUCH ROUTE ! \n")
    else:      
        if len(correct_result)==1:
            correct_dist_1=dist_list[int(correct_result[0])]
    
        print("Q 2 -- answer =  " + str(correct_dist_1))   
    
    #4. The distance of the route A-E-B-C-D.
    
    correct_result=[index for index,l in enumerate(paths_list) if len(l) == 5 and l[1] == 'E' and l[2] == 'B' and l[3] == 'C']
    if not correct_result:
        print("NO SUCH ROUTE ! \n")
    else:          
        if len(correct_result)==1:
            correct_dist_2=dist_list[int(correct_result[0])]    
        print("Q 4 -- answer =  " + str(correct_dist_2)) 
        
    #5. The distance of the route A-E-D.
 
    correct_result=[index for index,l in enumerate(paths_list) if len(l) == 3 and l[1] == 'E']
    if not correct_result:
        print("Q 5 -- answer :  NO SUCH ROUTE ! \n")
    else:    
        if len(correct_result)==1:
            correct_dist_3=dist_list[int(correct_result[0])]    
        print("Q 5 -- answer =  " + str(correct_dist_3)) 
 
 
    
    
    #6. The number of trips starting at C and ending at C with a maximum of 3
    #stops.  In the sample data below, there are two such trips: C-D-C (2
    #stops). and C-E-B-C (3 stops).
    
    
    ##***** FOR Q 2  & 6: *****    

    ##RESET a-C route values and re-do for A->D:
    paths_list=[]
    dist_list=[]
    num_town_list=[]
    visited =[False]*len(town_graph.nodes)
    # Call the recursive helper function to print all paths
    town_graph.printAllPathsUtil('C', 'C',visited, path_local)      

    
    bla=-1
    
#So rather than going down this rabbit hole, I guess it is maybe enough for me to use a non generalised solution (search)..?
    
    
    #9. The length of the shortest route (in terms of distance to travel) from B
    #to B.
    
    
    
    #10. The number of different routes from C to C with a distance of less than
    #30.     