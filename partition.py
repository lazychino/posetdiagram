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

def genPartitions(n, powerSet, tab="", partitions=[]):
	if n < 1:
		return powerset[1]
	else:
		print tab + "n =", n
		
		for i in range(1, n/2+1):
			#~ print tab,"i:", i
			print genPartitions(i, powerSet, tab + "  ")
			print [p for p in genPartitions(n-i, powerSet, tab + "  ")]
			for p1 in powerset[i]:
				for p2 in powerset[n-i]:
					#~ print "p1 %s | p2 %s" % (p1, p2)
					if p1.isdisjoint(p2):
						#~ print "acpt p1 %s | p2 %s" % (p1, p2)
						if [p1, p2] not in partitions and [p2, p1] not in partitions:
							partitions.append([p1,p2])
		print partitions
		return partitions

#~ partitions = genPartitions(n, powerset)

#for i in range(len(powerset)/2+1):
#	print i
#	print (len(powerset)-1)-i
#	for p1 in powerset[i]:
#			for p2 in powerset[(len(powerset)-1)-i]:
#				#~ print "p1 %s | p2 %s" % (p1, p2)
#				if p1.isdisjoint(p2):
#					#~ print "p1 %s | p2 %s" % (p1, p2)
#					if [p1, p2] not in partitions and [p2, p1] not in partitions:
#						partitions.append([p1,p2])

def numOfElements(L):
	cardinality = 0
	for s in L:
		cardinality += len(s)
	return cardinality
		
def version1(n, powerSet):
	#powerSet.pop(n)
	#powerSet.pop(0)
	partitions = []
	
	for i in range(1, n/2+1):
		#~ print "i: %s" % (powerSet[i])
		for k in range(2,len(powerSet)-i):
			#~ print "k: %s" % (powerSet[k])
			currentPartitions = []
			print "i:", i, "k:", k
			for p1 in powerSet[i]:
				for p2 in powerSet[k]:
					#~ print "p1 %s | p2 %s" % (p1, p2)
					if p1.isdisjoint(p2):
						#~ print "p1 %s | p2 %s" % (p1, p2)
						if [p1, p2] not in partitions and [p2, p1] not in partitions:
							currentPartitions.append([p1,p2])
			if n-(k+i) > 0:
				for x in range(1,(n-(k+i))+1):
					current = copy.deepcopy(currentPartitions)
					print "current:", current

					#~ for y in range(((n-(k+i))+1)-x):
					print "x:", x#, "y:", y
					for p in current:
						skip = False
						print p
						for st in powerSet[x]:
							disjoint = True
							print " ", p
							if not all(st.isdisjoint(s) for s in p):
								disjoint = False
							
							if disjoint:
								p.append(st)
							
							if numOfElements(p) == n:
								print "  ", p
								partitions.append(p)
								skip = True
								break
							#~ if skip:
								#~ break
			else:
				partitions += currentPartitions

	#~ print "p1"
	#~ for p in partitions:
		#~ print p
	#~ print "end"
	#~ print len(partitions)
	'''
	c = 0
	tmp = list()
	for p in partitions:
		cardinality = numOfElements(p)
		
		if cardinality < n:
			for i in range(1,n-cardinality+1):
				for c1 in powerSet[i]:
					disjoint = True
					for s in p:
						#~ print c1.isdisjoint(s)
						if not c1.isdisjoint(s):
							disjoint = False
							
					if disjoint:
						p.append(c1)
						
					if numOfElements(p) == n:
						#~ print p
						c += 1
						tmp.append(p)
		else:
			c+=1
			tmp.append(p)
			#~ print p

	#~ print "count", c, len(partitions)
	#~ for t in tmp:
			#~ print t
	#~ print len(tmp)
	'''
	tmp = partitions

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
	
	partitions = tmp
	
	tmp = list()
	for i in range(n):
		tmp.append(set([i]))
	partitions.append(tmp)
	partitions.append([set(range(n))])
	
	return partitions


#-----------------------------------------------------------------------

#powerset.pop(n)
#powerset.pop(0)
n = int(raw_input("entre n:"))

powerset = genPowerSet(n)

#~ print powerset

partitions = version1(n, powerset)

for p in partitions:
	print p
print len(partitions)









