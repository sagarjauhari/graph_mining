# Calculate performance metrics: separability, density, cohesiveness, clustering coefficient
# To run this code, execute:
# 		python GoodnessPerformanceMetrics.py communities.txt n p graph.txt
# where:
# 		communities.txt is the file containing the communities identified with the community detection algorithm
# 		n is the number of vertices in the graph
# 		p is the number of communities identified with the community detection algorithm.
#		graph.txt is the file containing the edge list of the graph,
# e.g., python GoodnessPerformanceMetrics.py communities.txt 6 3 graph.txt

import sys
import numpy
import math
import igraph
import itertools

def main(arg1, arg2, arg3, arg4):
    foundCluster = file(arg1,'r')
    numVertices = int(arg2)
    numberOfFoundCluster = int(arg3)
    graphObj = igraph.Graph.Read_Ncol(arg4,names=True)
    graphObj.to_undirected()

    foundClusterLines = foundCluster.readlines()
    foundClusterLines = [line.strip() for line in foundClusterLines]
    foundCluster.close()

    allDensity = 0.0
    allClusteringCoeff = 0.0
    allSeperation = 0.0
    allCohesion = 0.0

    for line in foundClusterLines:
	    line = line.strip()
	    column = line.split(" ")
	    vertexList = sorted(column)
	    vertexList = [int(x) for x in vertexList]
	    subgraphComm = graphObj.subgraph(vertexList)
	    vCount = subgraphComm.vcount()
	    if vCount>1:
		    allDensity = allDensity+subgraphComm.density()
	    else:
		    allDensity = allDensity+1
	    if subgraphComm.transitivity_undirected(mode="zero")==subgraphComm.transitivity_undirected(mode="zero"):
		    allClusteringCoeff = allClusteringCoeff+subgraphComm.transitivity_undirected(mode="zero")
	    inCount = 0
	    outCount = 0
	    for v in range(0,vCount):
		    inCount = inCount+len(subgraphComm.neighbors(v))
		    outCount = outCount+len(set(graphObj.neighbors(vertexList[v])).difference([vertexList[g] for g in subgraphComm.neighbors(v)]))
	    inCount = inCount/2.0
	    if outCount>0:
		    allSeperation = allSeperation+(inCount/outCount)
	    else:
		    allSeperation = allSeperation+inCount
	    allCohesion = allCohesion+subgraphComm.cohesion()
        
        
    avgDensity = allDensity/numberOfFoundCluster
    print("Density:\t\t"+str(round(avgDensity,4)))
    avgClusteringCoeff = allClusteringCoeff/numberOfFoundCluster
    print("Clustering Coefficient:\t"+str(round(avgClusteringCoeff,4)))
    avgSeperation = allSeperation/numberOfFoundCluster
    print("Separability:\t\t"+str(round(avgSeperation,4)))
    avgCohesion = allCohesion/numberOfFoundCluster
    print("Cohesiveness:\t\t"+str(round(avgCohesion,4)))
