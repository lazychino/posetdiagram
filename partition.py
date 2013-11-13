import itertools
import copy


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
	for i in range(1, n/2+1):
		#~ print "i: %s" % (powerSet[i])
		for k in range(i,len(powerSet)-i):
			#~ print "k: %s" % (powerSet[k])
			currentPartitions = []
			print "i:", i, "k:", k
			for p1 in powerSet[i]:
				for p2 in powerSet[k]:
					#~ print "p1 %s | p2 %s" % (p1, p2)
					if p1.isdisjoint(p2):
						#~ print "p1 %s | p2 %s" % (p1, p2)
						if [p1, p2] not in currentPartitions and [p2, p1] not in currentPartitions:
							#~ print "added"
							currentPartitions.append([p1,p2])
			#~ print currentPartitions
			if n-(k+i) > 0:
				for x in range(1,(n-(k+i))+1):
					current = copy.deepcopy(currentPartitions)
					#~ print "current:"

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
							
							if numOfElements(p) == n:
								#~ print "  accepted"
								if all(list(i) not in partitions for i in list(itertools.permutations(p,len(p)))):
									partitions.append(p)
								skip = True
								break
			else:
				partitions += currentPartitions

	partitions.append([set(range(n))])
	
	return partitions


def filterDuplicates(tmp):
	## filter duplicates
	i = 0
	sizeof = len(tmp)
	while i < sizeof:
		j = 0
		while j < sizeof:
			if len(tmp[i]) == len(tmp[j]) and j != i:
				#~ print tmp[i]
				#~ print tmp[j]
				same = 0
				for x in tmp[i]:
					skip = False
					for y in tmp[j]:
						if x == y:
							#~ print x
							#~ print y
							same += 1
							#~ print same
								
						if same == len(tmp[i]):
							#~ print "pop!"
							tmp.pop(j)
							j -= 1
							sizeof -= 1
							skip = True
							break
					if skip:
						break
			j += 1
		i +=1

	#~ for t in tmp:
			#~ print t
	#~ print len(tmp)
	
	return tmp



#-----------------------------------------------------------------------

#powerset.pop(n)
#powerset.pop(0)
n = int(raw_input("entre n:"))

powerset = genPowerSet(n)

#~ print powerset

partitions = setPartitions(n, powerset)
print len(partitions)
#~ partitions = filterDuplicates(partitions)  # not needed

partsize = []
partqty = []
for p in partitions:
	sz = list(len(s) for s in p)
	partqty.append(sz)
	if sz not in partsize:
		partsize.append(sz)


partition = partitions

#for par in partsize:
#	print par, partqty.count(par)

orderedpartitions = []
for i in range(n+1):
	orderedpartitions.append([])

for p in partition:
	m = 0
	for s in p:
		lens = len(s)
		if lens > m:
			m = lens
			mi = p.index(s)
	orderedpartitions[m].append(p)

for i in orderedpartitions:
	print i

for index in range(1,n):
	for i in orderedpartitions[index]:
		for j in orderedpartitions[index+1]:
			for k in :
			if i <= j:
			





