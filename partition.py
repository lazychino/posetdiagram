import itertools

powerset1 = list()

n = int(raw_input("entre n:"))


for i in range(n+1):

	powerset1.append(list(itertools.combinations(range(n),i)))
	
powerset = list()

for arr in powerset1:
	r = list()
	for elem in arr:
		r.append(set(elem))
	powerset.append(r)

powerset.pop(n)
powerset.pop(0)

#~ print powerset

partitions = []
for i in range(0, n/2):
	#~ print "i: %s" % (powerset[i])
	for k in range(1,len(powerset)-i):
		#~ print "k: %s" % (powerset[k])
		
		for p1 in powerset[i]:
			for p2 in powerset[k]:
				#~ print "p1 %s | p2 %s" % (p1, p2)
				if p1.isdisjoint(p2):
					#~ print "p1 %s | p2 %s" % (p1, p2)
					if [p1, p2] not in partitions and [p2, p1] not in partitions:
						partitions.append([p1,p2])

tmp = list()
for p in partitions:
	cardinality = 0
	for s in p:
		cardinality += len(s)
	
	if cardinality < n:
		for c1 in powerset[0]:
			disjoint = True
			for s in p:
				#~ print c1.isdisjoint(s)
				if not c1.isdisjoint(s):
					disjoint = False
				
			if disjoint:
				prt = list(p)
				prt.append(c1)
				tmp.append(prt)
	else:
		tmp.append(p)
		#~ print p

#~ print "temp"
#~ for t in tmp:
	#~ print t
#~ print len(tmp)

i = 0
sizeof = len(tmp)

while i < (sizeof-1):
	j = i+1
	while j < sizeof:
		if len(tmp[i]) == len(tmp[j]):
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
						sizeof -= 1
						skip = True
						break
				if skip:
					break
		j += 1
	i +=1

partitions = tmp

tmp = list()
for i in range(n):
	tmp.append(set([i]))
partitions.append(tmp)
partitions.append(set(range(n)))

for p in partitions:
	print p
print len(partitions)
