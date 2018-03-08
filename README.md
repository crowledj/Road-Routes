# Road-Routes
A python task that uses directed graphs to describe a routing system between neighbouring towns. Written in purely vanilla python.
               *********************************************************************
                    ***********************  SUMMARY :   ***********************
               *********************************************************************      

I decided to implement the Directed Graph model of the commuter route using a class based ?.
The graph its is implemented with a dictionary of lists - i.e the adjacency list method for storage and retrievaql of each node's neighbours.
I used the same data- structure for the other necessary structs - where the distances (weights) between towns (nodes) was donme using a nested 
dictionary of integers.

I chose to use a recursive method - "printAllPathsUtil()" to search through the graph and save all unique routes between  given start and end vertices(towns).

Then once all these routes were stored for a given start and destination pt., I could use these to answer the Qs relating to this (source,dest.)
Route. eg, min. dist , a given specific route.

This was done in this manner so that I traverse "all"  routes while achieving generality.
I also tracked visited nodes during this search so as to avoid cycles - which can lead to infinitely many solutions. 

               *********************************************************************
               ********************    RUNNING INSTRUCTIONS :   ********************
               *********************************************************************   
               
To run my code , all that is required is to ,

run from an IDE like Wing or Spyder with the follwing as arguments to the file roadGraphs.py :

                     AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
 
 or from a cmd line inc. python 3.5 in your PATH as :
 
                    python roadGraphs.py  AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
                    


                    
               


