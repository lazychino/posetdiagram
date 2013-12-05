from itertools import combinations, permutations
from threading import Thread


rtn = [] # global list for use as a stack for the thread

def distintJoin(P, P2, join):
    ''' makes a disjoint join of partion '''
    for p in P:        
        for p2 in P2:
            if all(x.isdisjoint(y) for x in p2 for y in p):
                tmp = p.union(p2)
                if all(not tmp.issubset(i) for i in join):
                    join.append(tmp)
    return join


def genCombinationOfSizeN(S, n):
    ''' this generate subsets of size n fron the set S '''
    rtn.append([frozenset([frozenset(x)]) for x in list(combinations(S,n))])


def SetPartitions(S):
    s = len(S)
    # generate elements of cardinality 1
    combi = list()
    combi.append([frozenset([frozenset([x])]) for x in S])
    
     # generate elements of cardinality 2
    combi.append([frozenset(x) for x in list(combinations([frozenset([x]) for x in S],2))])
    combi[1] += [frozenset([frozenset(x)]) for x in list(combinations(S,2))]
    
    for i in range(2,s):    # combi[i] have elements of cardinality i+1
        temp = list()
        tred = Thread(target=genCombinationOfSizeN, args= (S, i+1))  # parallelization
        tred.start()
        for k in range((i+1)/2):
            #combine subsets so that the sum of their cardinalities is equal to i
            temp = distintJoin(combi[i-(k+1)], combi[k], temp) 
        tred.join()
        temp += rtn.pop()
        combi.append(temp)
    
    return combi[s-1]


if __name__ == "__main__":
#--------------testing code-------------------------------- 
    import datetime
    print "Set partitions genarator"
    s = input("enter set(list or string): ")
    print "Set =", s
    t1 = datetime.datetime.today()
    parts = SetPartitions(s)
    t2 = datetime.datetime.today()


    print parts
    print 'total time', t2-t1
    print 'Set%s have %d partitions' % (list(s), len(parts))

    
