# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import itertools as iters
import linecache

import ConfusionMatrixMetrics
import GoodnessPerformanceMetrics
import NormalizedMutualInformation

try:
   from dev_settings import *
except ImportError:
   pass

# <codecell>

def do_perf():
    sets = ["amazon", "dblp", "youtube"]
    tests = ["2-2", "1-4", "4-2", "3-3"]
    
    for i in iters.product(sets, tests):
        if i[1]=="3-3":
            g_size="small"
        elif i[0]=="youtube" and i[1]=="2-2":
            g_size="large"
        else:
            g_size="original"
        
        comm_path = T_OUT+i[0]+".mycomm." + g_size+"_"+i[1]
        grnd_path = DATA+i[0]+".comm." + g_size
        grph_path = DATA+i[0]+".graph." + g_size
        
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
