# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import itertools as iters
import linecache

import ConfusionMatrixMetrics
import GoodnessPerformanceMetrics
import NormalizedMutualInformation

# <codecell>

def do_perf():
    sets = ["amazon", "dblp", "youtube"]
    tests = ["1-2", "3-3", "5-2"]
    
    for i in iters.product(sets, tests):
        comm_path = T_OUT+i[0]+".mycomm.small_"+i[1]
        grnd_path = DATA+i[0]+".comm.small"
        grph_path = DATA+i[0]+".graph.small"
        
        with open(grph_path, 'r') as f:
            n = next(f).split(' ')[0]
        with open(grnd_path) as f:
            k = sum(1 for line in f)
        with open(comm_path) as f:
            p = sum(1 for line in f)
        print "\n#####"+i[0]+"_"+i[1]
        ConfusionMatrixMetrics.main(grnd_path, comm_path, n, k, p)
        GoodnessPerformanceMetrics.main(comm_path, n, p, grph_path)
        NormalizedMutualInformation.main(grnd_path, comm_path, n, k, p)
do_perf()
