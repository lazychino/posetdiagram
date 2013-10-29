from datetime import datetime
from itertools import chain, combinations

def subsets(arr):
    """ Note this only returns non empty subsets of arr"""
    return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])

def k_subset(arr, k):
    s_arr = sorted(arr)
    return set([frozenset(i) for i in combinations(subsets(arr),k) 
               if sorted(chain(*i)) == s_arr])

partitions = []

n = 7
t1 = datetime.today()
for i in range(1,n+1):
    print i
    for p in k_subset(range(n),i):
        print p
        partitions.append(p)
t2 = datetime.today()

print t2-t1

print len(partitions)
for p in partitions:
    print p
