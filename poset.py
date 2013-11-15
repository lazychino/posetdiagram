import partitions

def orderSet(a, b):
    return len(a) - len(b)

def partiToString(S):  
    ''' convert partition to string representation '''
    return "|".join(["".join(str(e) for e in sorted(s)) for s in S])
    
def getRelations(Parts, n):
    ''' 
    returns a dictionary with the list of children for each partition on format part_1|part_2|...|part_n
    format example for set "abcd": a|b|cd
    '''
    
    orderedpartitions = [list() for i in range(n+1)]

    for p in Parts:
        p = list(p)
        m = len(p)
        p.sort(orderSet)
        p.reverse()
        orderedpartitions[m].append(p)

    orderedpartitions.pop(0)
    orderedpartitions.reverse()

    posetDict= dict()
    for i in reversed(range(1,n)):
        for x in orderedpartitions[i]:
            posetDict[partiToString(x)] = []
            if (i-1) == 0:
                posetDict[partiToString(x)].append(partiToString(orderedpartitions[0][0]))
            else:
                for y in orderedpartitions[i-1]:
                    if any(y[0].issubset(s) for s in x if len(s) > 1):
                        posetDict[partiToString(x)].append(partiToString(y))
    posetDict[partiToString(orderedpartitions[0][0])] = None
    posetDict['root'] = partiToString(orderedpartitions[n-1][0])
    return posetDict

def toJSON(P, parent):
    if P[parent] == None:
        return '{ "name": "%s" }' % (parent)
    else:
        arr = []
        for child in P[parent]:
            arr.append(toJSON(P, child))
        children = ",".join(arr)
        return '{ "name": "%s", "children": [ %s ] }' % (parent, children)

def getDiagramPosetOf(S):
    ''' takes a antichain set and return the poset for all posible equivalent diagrams '''
    parts = partitions.SetPartitions(S)
    poset = getRelations(parts, len(S))
    return toJSON(poset, poset['root'])
 
#---------testing code ----------------------
#~ SET = 'abcd'
#~ f = open("poset.json", 'w')
#~ f.write(getDiagramPosetOf(SET))
#~ f.close()



