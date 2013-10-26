Below you will find 3 scripts to compute performance metrics for community detection algorithms. You will use these scripts to evaluate the community detection algorithm you implemented for Project 1.

Note that all scripts are in Python. If you want to write your own scripts in any other programming language, feel free to do so, but make sure you include the codes in your final submission

The notion of “good” communities will be tested using the following performance metrics:

[DOWNLOAD CODE HERE: Link]

    Separability: captures the intuition that good communities are well-separated from the rest of the network.
    Density: builds on the intuition that good communities are well connected.
    Cohesiveness: characterizes the internal structure of the community. Intuitively, a good community should be internally well and evenly connected, i.e., it should be relatively hard to split a community into two subcommunities.
    Clustering coefficient: is a measure of the degree to which the nodes in a graph tend to cluster together.

The conformance of the identified communities to the ground truth communities will be tested using the following performance metrics:

    Precision [DOWNLOAD CODE FOR METRICS 1-5 HERE: Link]
    Recall
    F-measure
    Specificity
    RAND Index
    Normalized Mutual Information [DOWNLOAD CODE FOR METRIC 6 HERE: Link]

To run these codes, execute the following commands:

python GoodnessPerformanceMetrics.py communities.txt n p graph.txt

python ConfusionMatrixMetrics.py ground_truth.txt communities.txt n k p

python NormalizedMutualInformation.py ground_truth.txt communities.txt n k p

where ground_truth.txt is the file containing the ground truth communities, communities.txt is the file containing the communities identified with the community detection algorithm, graph.txt is the file containing the edge list of the graph, n is the number of vertices in the graph, k is the number of ground truth communities and p is the number of communities identified with the community detection algorithm.

An example dataset you can use to test these codes, is attached:

    Graph A [Link]
    Communities of Graph A [Link]
    Ground Truth of Graph A [Link]

Additional resources:

    A modified version of Normalized Mutual Information [DOWNLOAD CODE HERE: Link]  [PAPER AVAILABLE HERE: Link]
    Python iGraph package tutorial [URL: Link]


