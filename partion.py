import itertools

powerset = list()

n = 4

for i in range(n+1):

	powerset.append(list(itertools.combinations(range(n),i)))


partitions = list()

for arr in powerset:
	for elem in arr:
		print list(elem)
#--------------------------------------------------------------------
# hasta aqui tenemos el power set


