import itertools
import copy
import sys

def genPowerSet(n):
    powerset1 = list()
    for i in range(n+1):
        powerset1.append(list(itertools.combinations(range(n),i)))
        
    powerset = list()

    for arr in powerset1:
        r = list()
        for elem in arr:
            r.append(set(elem))
        powerset.append(r)
    
    return powerset

def numOfElements(L):
    cardinality = 0
    for s in L:
        cardinality += len(s)
    return cardinality

def setPartitions(n, powerSet):
    partitions = []
    for i in range(1, (n/2)+1):
        for k in range(i,(n+1)-i):  #combine partition of size i with every partition of size k where where k+i <= n
            currentPartitions = []
            print "i:", i, "k:", k
            if i == 1 and k == 1:
                continue
            for p1 in powerSet[i]:
                for p2 in powerSet[k]:
                    #~ print "p1 %s | p2 %s" % (p1, p2)
                    if p1.isdisjoint(p2):
                        #~ print "p1 %s | p2 %s" % (p1, p2)
                        if [p1, p2] not in currentPartitions and [p2, p1] not in currentPartitions:
                            #~ print "added"
                            currentPartitions.append([p1,p2])
            count = 0
            count2 = 0
            if n-(k+i) > 0:
                for x in range(1,(n-(k+i)+1)):
                    current = copy.deepcopy(currentPartitions)
                    done = False
                    while(not done):
                        print current
                        current = distintJoin(current, powerset[x])
                        for p in current:
                            if numOfElements(p) == n:
                                if not done:
                                    done = True
                                    print 'done'
                                if all(list(i) not in partitions for i in list(itertools.permutations(p,len(p)))):
                                    partitions.append(p)
            else:
                partitions += currentPartitions

    partitions.append([set([n]) for n in range(n)])
    partitions.append([set(range(n))])
    
    return partitions

def distintJoin(P, sets):
    join = []
    for prt in P:
        p = list(prt)
        for st in sets:
            temp = copy.deepcopy(p)
            if all(st.isdisjoint(s) for s in p):
                temp.append(st)
                join.append(temp)
    return join
    
'''
for p in current:
    skip = False
    #~ print p
    for st in powerSet[x]:
        disjoint = True
        #~ print " ", st
        if not all(st.isdisjoint(s) for s in p):
            disjoint = False
        
        if disjoint:
            #~ print "  appened"
            p.append(st)
        #~ if i == 1 and k == 2 and x == 2:
            #~ print p
        if numOfElements(p) == n:
            #~ if i == 1 and k == 2 and x == 2:
                #~ for l in list(itertools.permutations(p,len(p))):
                    #~ l = list(l)
                    #~ if l in partitions:
                        #~ print l, ' ', l in partitions
            if all(list(i) not in partitions for i in list(itertools.permutations(p,len(p)))):
                partitions.append(p)
                if i == 1 and k == 2 and x == 2:
                    #~ print "  accepted"
                    count += 1
                    print p
            #~ if i == 1 and k == 2 and x == 2:
                #~ count2 += 1
                #~ print 'c1',count
                #~ print 'c2',count2
            #~ skip = True
            break
'''

def orderSet(a, b):
    return len(a) - len(b)

#-----------------------------------------------------------------------

#powerset.pop(n)
#powerset.pop(0)
n = int(raw_input("entre n:"))

powerset = genPowerSet(n)

partitions = setPartitions(n, powerset)

for p in partitions:
    print p
print len(partitions)

#------------------debuging size of each partition-----------------
#~ partsize = []
#~ partqty = []
#~ for p in partitions:        
    #~ sz = list(len(s) for s in p)
    #~ partqty.append(sz)
    #~ if sz not in partsize:
        #~ partsize.append(sz)

#for par in partsize:
#   print par, partqty.count(par)


# ----------------end debug----------------------------------------




