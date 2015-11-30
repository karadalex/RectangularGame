import sys

N = int(raw_input().strip())
a,b = raw_input().strip().split(' ')
a,b = [int(a), int(b)]
iDimension = a
jDimension = b
for n in xrange(N-1):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a), int(b)]
    iDimension = min(iDimension, a)
    jDimension = min(jDimension, b)

numOfMax = iDimension*jDimension
print numOfMax
