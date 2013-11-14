orderedpartitions = []
for i in range(n+1):
    orderedpartitions.append([])

#~ print partitions

for p in partitions:
    m = len(p)
    p.sort()
    p.reverse()
    orderedpartitions[m].append(p)

orderedpartitions.pop(0)
orderedpartitions.reverse()

#~ print orderedpartitions
for i in orderedpartitions:
    print i


print "\n\nPOSET"
for i in reversed(range(2,n)):
    for x in orderedpartitions[i]:
        print '\n', x, '->',
        for y in orderedpartitions[i-1]:
            if y[0].issubset(x[0]):
                print y, ' ',
        sys.stdout.flush()
