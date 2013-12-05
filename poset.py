import partitions
import json

def orderSet(a, b):
    ''' order element of partitions '''
    if( len(a) == 1 and len(b) == 1):
        return list(b)[0] - list(a)[0]
        
    return len(a) - len(b)

def partiToString(S):  
    ''' convert partition to string representation '''
    return "|".join(["".join(str(e) for e in sorted(s)) for s in S])

def partToDict(p, level):
    ''' create node object '''
    return {'name': partiToString(p), 'level': level }

def getRelations(Parts, n):
    ''' 
    returns a dictionary with the list of nodes and list of links, 
    each node have the level on the poset and its string respresentation 
    string format: part_1|part_2|...|part_n 
    format example partititon {{a},{b},{c,d}} = "a|b|cd"
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
            if partX not in nodes:   #check if partition is on graph nodes list
                nodes.append(partX)
            if (i-1) == 0: #if next node is null link to it
                links.append({ 'source': nodes.index(partX), 'target': nodes.index(partToDict(orderedpartitions[0][0], 0))})
            else:
                for y in orderedpartitions[i-1]:
                    partY = partToDict(y,(i-1))
                    if partY not in nodes: 
                        nodes.append(partY)
                    if any(y[0].issubset(s) for s in x if len(s) > 1): # if partitionY is subset of partitionX create a link between nodes
                        links.append({ 'source': nodes.index(partX), 'target': nodes.index(partY) })
    return {'nodes': nodes, 'links': links }

def toJSONTree(P, parent): #not used
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
    import datetime
    print "Antichain poset of diagram genarator"
    antichain = input("enter antichain size:")
    t1 = datetime.datetime.today()
    poset = getDiagramPosetOf(range(antichain))
    t2 = datetime.datetime.today()
    f = open("poset.json", 'w')
    f.write(poset)
    print "the poset is on JSON format in the file 'poset.json'"
    f.close()
    print 'time to generate', t2-t1
