# Calculate performance metrics: recall, precision, F-measure, specificity and RAND Index
# To run this code, execute:
# 		python ConfusionMatrixMetrics.py ground_truth.txt communities.txt n k p
# where:
#		ground_truth.txt is the file containing the ground truth communities,
# 		communities.txt is the file containing the communities identified with the community detection algorithm
# 		n is the number of vertices in the graph
# 		k is the number of ground truth communities
# 		p is the number of communities identified with the community detection algorithm.
# e.g., python ConfusionMatrixMetrics.py ground_truth.txt communities.txt 6 2 3

import sys
import numpy
import math
import itertools

def choose(n,k):
# A fast way to calculate binomial coefficients by Andrew Dalke
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def main(arg1, arg2, arg3, arg4, arg5):
    groundTruth            = file(arg1,'r')
    foundCluster           = file(arg2,'r')
    numVertices            = int( arg3)
    numberOfGroundTruth    = int( arg4)
    numberOfFoundCluster   = int( arg5)

    vertexList = [str(i) for i in range(0,(numVertices))]
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

    vertexGroundTruthPairs = []
    vertexFoundClusterPairs = []

    for line in groundTruthLines:
        line = line.strip()
        column = line.split(" ")
        vertexGroundTruthPairs.extend(list(itertools.combinations(sorted(column), 2)))
       
    vertexGroundTruthPairsUnique = set(vertexGroundTruthPairs)   

    for line in foundClusterLines:
        line = line.strip()
        column = line.split(" ")
        vertexFoundClusterPairs.extend(list(itertools.combinations(sorted(column), 2)))
     
    vertexFoundClusterPairsUnique=set(vertexFoundClusterPairs)

    TruePositive = float(len(vertexGroundTruthPairsUnique.intersection(vertexFoundClusterPairsUnique)))
    FalsePositive = float(len(vertexFoundClusterPairsUnique.difference(vertexGroundTruthPairsUnique)))
    FalseNegative = float(len(vertexGroundTruthPairsUnique.difference(vertexFoundClusterPairsUnique)))
    TrueNegative = (choose(numVertices,2))-(TruePositive+FalsePositive+FalseNegative)

    Recall = TruePositive/(TruePositive+FalseNegative)
    Precision = TruePositive/(TruePositive+FalsePositive)
    FMeasure = (2*Precision*Recall)/(Precision+Recall)
    Specificity = TrueNegative/(TrueNegative+FalsePositive)
    RANDIndex = (TruePositive+TrueNegative)/(TruePositive+FalsePositive+FalseNegative+TrueNegative)

    print('True Positive:\t'+str(round(TruePositive,4)))
    print('False Positive:\t'+str(round(FalsePositive,4)))
    print('False Negative:\t'+str(round(FalseNegative,4)))
    print('True Negative:\t'+str(round(TrueNegative,4)))
    print('Recall:\t\t'+str(round(Recall,4)))
    print('Precision:\t'+str(round(Precision,4)))
    print('F-Measure:\t'+str(round(FMeasure,4)))
    print('Specificity:\t'+str(round(Specificity,4)))
    print('RAND Index:\t'+str(round(RANDIndex,4)))

#if __name__=='__main__':
#    sys.exit(main(sys.argv[1], sys.argv[2]))
