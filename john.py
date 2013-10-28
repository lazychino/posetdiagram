import itertools
import copy


def genPowerSet2(n):
	powerset1 = list()
	for i in range(n+1):
		powerset1.append(list(itertools.combinations(range(n),i)))
		
	powerset = list()

	for x in range(1,len(powerset1)-1):
		for elem in powerset1[x]:
			powerset.append([set(elem)])
	
	return powerset

n = input("entre n:")

powerset = genPowerSet(n)

listagigante = list()


for i in range(n):
	for x in powerset:
		for y in powerset:
			x.append(y)
