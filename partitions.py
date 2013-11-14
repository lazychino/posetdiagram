from itertools import combinations, permutations
import copy
import datetime

def distintJoin(P, sets, join):
    for p in P:        
        for st in sets:
            temp = copy.deepcopy(p)
            #~ print 'st', st
            #~ print 'p ', p
            if all(x.isdisjoint(y) for x in st for y in p):
                #~ print '   disjoint'
                temp = temp.union(st)
                if all(not temp.issubset(p) for p in join):
                    join.append(temp)
    return join

def SetPartitions(S):
    s = len(S)
    combi = list()
    combi.append([frozenset([frozenset([x])]) for x in S])

    combi.append([frozenset(x) for x in list(combinations([frozenset([x]) for x in S],2))])
    combi[1] += [frozenset([frozenset(x)]) for x in list(combinations(S,2))]
        
    for i in range(2,s):    # combi[i] have element of cardinality i+1
        temp = []
        for k in range((i+1)/2):
            temp = distintJoin(combi[i-(k+1)], combi[k], temp)
        temp += [frozenset([frozenset(x)]) for x in list(combinations(S,i+1))]
        combi.append(copy.deepcopy(temp))
        del temp
    
    return combi[s-1]

#~ n = input('enter n:')
#~ 
#~ t1 = datetime.datetime.today()
#~ parts = SetPartitions(range(n))
#~ t2 = datetime.datetime.today()
#~ 
#~ 
#~ print parts
#~ print 'total time', t2-t1
#~ print 'combi[%d] size=%d' % (n, len(parts))

    
