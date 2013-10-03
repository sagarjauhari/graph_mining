# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Graph Data Mining - Lecture Assignment 1
# #### Sagar Jauhari (sjauhar)
# #### HW Buddy: Vandit Khamker (vkhamke)
# #### HW Buddy: Navya Pedemane(nmpedema)

# <codecell>

from igraph import *
import numpy as np
import matplotlib.pyplot as plt
import math

# <markdowncell>

# ##Exercise 1 Generating the adjacency matrix A for graphs of particular type.
# Write a script (in R, Matlab, or SAS) that generates the adjacency matrix A for each of
# the following graphs and prints this matrix onto the screen:

# <markdowncell>

# ####(a) K5: 5-clique, or a fully connected simple, undirected graph of 5 nodes

# <codecell>

gk5 = Graph.Full(5);
gk5.get_adjacency()

# <markdowncell>

# ####(b) K5.3: two disconnected components, C1 and C2, where C1 is a 5-clique K5 and C2 is a 3-clique K3

# <codecell>

gc1 = Graph.Full(5)
gc2 = Graph.Full(3)
gk5_3 = gc1 + gc2
gk5_3.get_adjacency()

# <markdowncell>

# ####(c) K5.3e: Almost the same as K53 but there is a single edge connecting the two components

# <codecell>

gc3 = Graph.Full(5)
gc4 = Graph.Full(3)
gk5_3e = gc3 + gc4
gk5_3e.add_edge(1,5);
gk5_3e.get_adjacency()

# <markdowncell>

# ####(d) B2.3: Complete bi-partite graph with n1=2 nodes in the first part and n2=3 nodes in the second part

# <codecell>

gb2_3 = Graph.Full_Bipartite(2, 3)
gb2_3.get_adjacency()

# <markdowncell>

# ####(e) S5: A 5-vertex star (one central "hub" node that connects to all the other "spoke" nodes)

# <codecell>

gs5 = Graph.Star(5)
gb2_3.get_adjacency()

# <markdowncell>

# ####(f) P5: A simple path of 5 vertices

# <codecell>

gp5 = Graph()
gp5.add_vertices(5)
gp5.add_edges([(0,1),(1,2),(2,3),(3,4)])
gp5.get_adjacency()

# <markdowncell>

# ##Exercise 2: Generating the degree matrix D for a given adjacency matrix A.
# Write a script that generates a degree matrix for each of the adjacency matrices in
# Exercise 1. Note that the degree matrix is a diagonal matrix where all the positions
# except for the diagonal are zero's. The diagonal elements correspond to the degrees
# of the corresponding nodes, namely Dii = degree(v_i).

# <codecell>

def get_deg_matrix(graph):
    v = graph.vcount()
    a = np.zeros(shape=(v,v))
    for i in xrange(0,v):
        a[i][i]=graph.degree(i)
    return a

# <markdowncell>

# ####K5

# <codecell>

get_deg_matrix(gk5)

# <markdowncell>

# ####K5.3

# <codecell>

get_deg_matrix(gk5_3)

# <markdowncell>

# ####K5.3e

# <codecell>

get_deg_matrix(gk5_3e)

# <markdowncell>

# ####B2.3

# <codecell>

get_deg_matrix(gb2_3)

# <markdowncell>

# ####S5

# <codecell>

get_deg_matrix(gs5)

# <markdowncell>

# ####P5

# <codecell>

get_deg_matrix(gp5)

# <markdowncell>

# ##Exercise 3: Generating the graph Laplacian matrix L for a given adjacency matrix A and its degree matrix D. 
# Write a script that generates the graph
# Laplacian matrix L = D - A for each of the adjacency matrices in Exercise 1. Answer
# the following questions:

# <markdowncell>

# ### Over all answers:
# ####(a) Is L a sparse matrix?
# No, not for any of the cases
# ####(b) In what positions does L have non-zero elements?
# L has non-zero elements at places where there is an edge in the graph and the diagonal elementss (which represents the degree of the vertex)
# ####(c) What are the values of the non-diagonal and non-zero elements?
# -1
# ####(d) What does L contain along its diagonal?
# The degree of the corresponding vertex  
# #### (Individual answers below:)

# <markdowncell>

# ####K5

# <codecell>

gk5.laplacian()

# <markdowncell>

# ####(a) Is L a sparse matrix?
# No
# ####(b) In what positions does L have non-zero elements?
# All
# ####(c) What are the values of the non-diagonal and non-zero elements?
# Non-diagonal values = -1  
# Non - Zero values = 4
# ####(d) What does L contain along its diagonal?
# Diagonal = 4

# <markdowncell>

# ####K5.3

# <codecell>

gk5_3.laplacian()

# <markdowncell>

# ####(a) Is L a sparse matrix?
# No
# ####(b) In what positions does L have non-zero elements?
# Top Left 5x5 and Lower right 3x3
# ####(c) What are the values of the non-diagonal and non-zero elements?
# Non-diagonal values = 0,-1,2  
# Non-zero values = -1, 4, 2
# ####(d) What does L contain along its diagonal?
# Diagonal values = 4,2

# <markdowncell>

# ####K5.3e

# <codecell>

gk5_3e.laplacian()

# <markdowncell>

# ####(a) Is L a sparse matrix?
# No
# ####(b) In what positions does L have non-zero elements?
# Top left and lower right
# ####(c) What are the values of the non-diagonal and non-zero elements?
# Non-diagonal values = 0,-1  
# Non - zero values = -1,2,3,4,5
# ####(d) What does L contain along its diagonal?
# Diagonal values = 2,3,4,5

# <markdowncell>

# ####B2.3

# <codecell>

gb2_3.laplacian()

# <markdowncell>

# ####(a) Is L a sparse matrix?
# No
# ####(b) In what positions does L have non-zero elements?
# Almost all
# ####(c) What are the values of the non-diagonal and non-zero elements?
# non-diagonal values = 0,-1  
# non-zero values = -1,2,3
# ####(d) What does L contain along its diagonal?
# diagonal values = 3,2

# <markdowncell>

# ####S5

# <codecell>

gs5.laplacian()

# <markdowncell>

# ####(a) Is L a sparse matrix?
# No
# ####(b) In what positions does L have non-zero elements?
# top most row, left most column and diagonal
# ####(c) What are the values of the non-diagonal and non-zero elements?
# non-diagonal values = -1,4  
# non-zero values = -1, 1, 4
# ####(d) What does L contain along its diagonal?
# 4,1

# <markdowncell>

# ####P5

# <codecell>

gp5.laplacian()

# <markdowncell>

# ####(a) Is L a sparse matrix?
# No
# ####(b) In what positions does L have non-zero elements?
# The diagonal, and the diagonal values above and below it
# ####(c) What are the values of the non-diagonal and non-zero elements?
# non-diagonal values = 0,-1  
# non-zero values = -1,1,2
# ####(d) What does L contain along its diagonal?
# diagonal values = 1,2

# <markdowncell>

# ##Exercise 4: Generating the graph spectrum, or the multiset of the eigenvalues of the graph adjacency matrix A. 
# Write a script that calculates the eigenvalues of
# the graph adjacency matrix for each of the matrices in Exercise 2. Plot the
# eigenvalues in the increasing order of their values. Answer the following questions:

# <codecell>

def plot_eig(graph):
    e = np.sort(np.linalg.eig(graph.get_adjacency().data)[0])
    print ["%0.3f" % item for item in e]
    plt.plot(e)
    plt.ylabel('Eigen Values')
    plt.show()

# <markdowncell>

# ####K5

# <codecell>

plot_eig(gk5)

# <markdowncell>

# ####K5.3

# <codecell>

plot_eig(gk5_3)

# <markdowncell>

# ####K5.3e

# <codecell>

plot_eig(gk5_3e)

# <markdowncell>

# ####B2.3

# <codecell>

plot_eig(gb2_3)

# <markdowncell>

# ####S5

# <codecell>

plot_eig(gs5)

# <markdowncell>

# ####P5

# <codecell>

plot_eig(gp5)

# <markdowncell>

# ####(a) What can you say about the eigenvalues of the complete graph (K5): the number of unique eigenvalues, the largest and the smallest eigenvalues, the multiplicity (how many times the same egenvalue appears) of each eigenvalue?
# Number of unique eigenvalues = 2  
# Largest = 4  
# Smallest = -1  
# Multiplicity = -1: 4, 4: 1  

# <markdowncell>

# ####(b) What is the graph spectrum of the bi-partite graph, B2.3? If n1 = n and n2 = m (a general complete bi-partite graph), then what can you say about its graph spectrum? [Hint: check sqrt(n * m)] If \lambda is the eigenvalue of the bi-partite graph, will minus \lambda be also the eigenvalue?
# Spectrum =  {-|\sqrt(6)|, 0 , + |\sqrt(6)|}.   
# For a general complete bi-partite graph, graph spectrum = {-|sqrt(n*m)|, 0 , + |sqrt(n*m)|}  
# Yes. If \lambda is the eigenvalue then minus \lambda will also be its eigenvalue.

# <markdowncell>

# ####(c) What is the largest eigenvalue of the star graph S5? If S5 were generalized to an N-vertex star, what could you say about the value of its largest eigenvalue?
# Largest eigenvalue = 2  

# <codecell>

print '%2s %3s %4s' % ("n","E","E^2")
for i in xrange(2,10):
    g = Graph.Star(i)
    largest_eig = np.sort(np.linalg.eig(g.get_adjacency().data)[0])[-1]
    print '%2d %0.2f %0.2f' % (i,largest_eig,math.pow(largest_eig,2))

# <markdowncell>

# So, if S5 were generalized to an N-vertex star, the lagest eigen value has the relation:  
# ###Largest Eigen Value = sqrt(N-1)

# <markdowncell>

# ####(d) What is the largest eigenvalue of the star graph P5? As the length of the path increases, what can you say about the the changes in the largest eigenvalue?
# Largest Eigen Value of P5 = 1.73

# <codecell>

print '%2s %4s %4s' % ("n","E","E^2")
for i in xrange(2,10):
    g = Graph()
    g.add_vertices(i)
    for j in xrange(0,i-1):
        g.add_edge(j,j+1)
    largest_eig = np.sort(np.linalg.eig(g.get_adjacency().data)[0])[-1]
    print '%2d %0.3f %0.3f' % (i,largest_eig,math.pow(largest_eig,2))

# <markdowncell>

# Largest eigen value increases with the increment in n

# <markdowncell>

# ####(e) How does the largest eigenvalue of the path P5 (or its more generalization to an arbitrary length) compare with the largest eigenvalues of the star graph or the complete graph? If you are asked to sort the largest eigevalue of the path, the star, and the clique) in the increasing order, what kind of relationship would you assign (E.g., \lambda{path} > or < than \lambda{star})?

# <codecell>

print "%s\n"% ("Largest Eigen values:")
print '%2s %6s %6s %6s' % ("n","Full","Star","Path")
for i in xrange(2,10):
    g = Graph.Full(i)
    e1 = np.sort(np.linalg.eig(g.get_adjacency().data)[0])[-1]
    
    g = Graph.Star(i)
    e2 = np.sort(np.linalg.eig(g.get_adjacency().data)[0])[-1]
    
    g = Graph() 
    g.add_vertices(i)
    for j in xrange(0,i-1):
        g.add_edge(j,j+1)
    e3 = np.sort(np.linalg.eig(g.get_adjacency().data)[0])[-1]
       
    print '%2d  %0.3f  %0.3f  %0.3f' % (i,e1,e2,e3)

# <markdowncell>

# So, 
# #### \lambda{full} > \lambda{star} > \lambda{path}

# <markdowncell>

# ##Exercise 5: Generating the graph spectrum, or the multiset of the eigenvalues of the graph Laplacian. 
# Write a script that calculates the eigenvalues of the graph
# Laplacian for each of the graphs in Exercise 1. Plot the eigenvalues in the increasing
# order of their values. Answer the following questions:

# <codecell>

def plot_eig_lap(graph):
    e = np.sort(np.linalg.eig(graph.laplacian())[0])
    print ["%0.3f" % m for m in e]
    plt.plot(e)
    plt.ylabel('Eigen Values')
    plt.show()

# <codecell>

print "K5:"
plot_eig_lap(gk5)

print "K5.3"
plot_eig_lap(gk5_3)

print "K5.3e"
plot_eig_lap(gk5_3e)

print "B2.3"
plot_eig_lap(gb2_3)

print "S5"
plot_eig_lap(gs5)

print "P5"
plot_eig_lap(gp5)

# <markdowncell>

# ####(a) What can you say about the largest and the smallest eigenvalues?
# K5: largest = 0; smallest = 5;  
# K5.3: largest = 0; smallest = 5;  
# K5.3e: largest = 0; smallest = 6.141;  
# B2.3: largest = 0 smallest = 5;  
# S5: largest = 0; smallest = 5;  
# P5: largest = 0; smallest = 3.618;
# ####(b) What is the multiplicity (how many times the same egenvalue appears) of the zero eigenvalue for each of the cases?
# K5: 1  
# K5.3: 2  
# K5.3e: 1  
# B2.3: 1  
# S5: 1  
# P5: 1
# ####(c) If K53 graph would be generalized to include c>2 components, what can you say about the multiplicity of the zero eigenvalues?

# <codecell>

g = Graph.Full(2)
for i in xrange(2,10):
    g = g + Graph.Full(2)
    eigs = np.linalg.eig(g.laplacian())[0]
    print ["%0.2f" % eig for eig in eigs]

# <markdowncell>

# ####As components are added, it can be seen that the multiplicity of the eigen value '0' is equal to the number of disjoint components

# <markdowncell>

# ####(d) If graph G is connected (i.e., the number of disconnected components is one), what can you say about the multiplicity of the zero eigenvalue?
# One
# ####(e) For the bi-partite graph, what is the value of the second eigenvalue?
# 2
# ####(f) Is the vector consisting of only 1's the eigenvector of the Laplacian? If it is, then what is its corresponding eigenvalue?
# Yes, corresponding value = 0
# 
# ####(g) Suppose the graph Laplacian matrix has the zero eigenvalue of multiplicity k. Can you say anything about the structure of such a graph?
# K unconnected components

