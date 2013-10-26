# Calculate performance metrics: Normalized Mutual Information
# To run this code, execute:
# 		python NormalizedMutualInformation.py ground_truth.txt communities.txt n k p
# where:
#		ground_truth.txt is the file containing the ground truth communities,
# 		communities.txt is the file containing the communities identified with the community detection algorithm
# 		n is the number of vertices in the graph
# 		k is the number of ground truth communities
# 		p is the number of communities identified with the community detection algorithm.
# e.g., python NormalizedMutualInformation.py ground_truth.txt communities.txt 6 2 3

import sys
import numpy
import math

def main(arg1, arg2, arg3, arg4, arg5):
    groundTruth = file(arg1,'r')
    foundCluster = file(arg2,'r')
    numVertices = int(arg3)
    numberOfGroundTruth = int(arg4)
    numberOfFoundCluster = int(arg5)

    foundClusterSize = {}
    groundTruthSize = {}
    sumGroudTruth = 0
    sumFoundCluster = 0
    sumBoth = 0
    clusterOverlapTable = {}
    groundTruthLines = groundTruth.readlines()
    groundTruthLines = [line.strip() for line in groundTruthLines]
    groundTruth.close() 
    foundClusterLines = foundCluster.readlines()
    foundClusterLines = [line.strip() for line in foundClusterLines]
    foundCluster.close()

    i = 1
    for line in groundTruthLines:
        line = line.strip()
        column = line.split(" ")
        groundTruthSize[i] = float(len(column))
        sumGroudTruth = sumGroudTruth+(groundTruthSize[i]*math.log((groundTruthSize[i]/numVertices)))    
        i = i+1
       
    i = 1    
    for line in foundClusterLines:
        line = line.strip()
        column = line.split(" ")
        foundClusterSize[i] = float(len(column))
        sumFoundCluster = sumFoundCluster+(foundClusterSize[i]*math.log((foundClusterSize[i]/numVertices)))   
        i = i+1

    i = 1
    j = 1
    for line in groundTruthLines:
        line = line.strip()
        column = line.split(" ")
        j = 1
        for lineA in foundClusterLines:
            lineA = lineA.strip()
            columnA = lineA.split(" ")
            clusterOverlapTable[i,j] = float(len(set(column).intersection(set(columnA))))
            if(clusterOverlapTable[i,j]>0):
                sumBoth = sumBoth+(clusterOverlapTable[i,j])*math.log((numVertices*clusterOverlapTable[i,j])/(groundTruthSize[i]*foundClusterSize[j]))
            j = j+1
        i = i+1
        foundCluster.close()
        foundCluster = file(arg2,'r')
       
    NMI = sumBoth/(math.sqrt(sumGroudTruth*sumFoundCluster ))
    print('Normalized Mutual Information:\t'+ str(round(NMI,4)))
