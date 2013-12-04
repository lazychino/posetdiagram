import partitions
import json

def orderSet(a, b):
    if( len(a) == 1 and len(b) == 1):
        return list(b)[0] - list(a)[0]
        
    return len(a) - len(b)

def partiToString(S):  
    ''' convert partition to string representation '''
    return "|".join(["".join(str(e) for e in sorted(s)) for s in S])

def partToDict(p, level):
    return {'name': partiToString(p), 'level': level }

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
    
    nodes = []
    links = []
    
    nodes.append(partToDict(orderedpartitions[0][0], 0))
    
    for i in reversed(range(1,n)):
        for x in orderedpartitions[i]:
            partX = partToDict(x,i)
            if partX not in nodes:
                nodes.append(partX)
            if (i-1) == 0:
                links.append({ 'source': nodes.index(partX), 'target': nodes.index(partToDict(orderedpartitions[0][0], 0))})
            else:
                for y in orderedpartitions[i-1]:
                    partY = partToDict(y,(i-1))
                    if partY not in nodes:
                        nodes.append(partY)
                    if any(y[0].issubset(s) for s in x if len(s) > 1):
                        links.append({ 'source': nodes.index(partX), 'target': nodes.index(partY) })
    return {'nodes': nodes, 'links': links }

def toJSONTree(P, parent):
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
    return json.JSONEncoder().encode(getRelations(parts, len(S)))
    
 

if __name__ == "__main__":
#---------testing code ----------------------
    print "Antichain poset of diagram genarator"
    antichain = input("enter antichain size:")
    poset = getDiagramPosetOf(range(antichain))
    print poset
    f = open("poset.json", 'w')
    f.write(poset)
    print "the poset is on JSON format in the file 'poset.json'"
    f.close()
