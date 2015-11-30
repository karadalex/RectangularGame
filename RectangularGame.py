import sys

Grid = [[]]
N = int(raw_input().strip())
for n in xrange(N):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a), int(b)]
    for i in xrange(a):
        for j in xrange(b):
            while True:
                try:
                    Grid[i][j] += 1
                    break
                except IndexError:
                    try:
                        Grid[i].append(0)
                    except IndexError:
                        Grid.append([0])


#the cell (1,1) of the board always contains the maximum number
#the following code is an effort to make an optimized search of maximums throughout Grid
maximum = Grid[0][0]
numOfMax = 0
i = 0
j = 0
while i <= 1000000:
    while j <= 1000000:
        try:
            if Grid[i][j] == maximum:
                numOfMax += 1
        except IndexError:
            break
        try:
            if Grid[i][j+1] < maximum:
                break
        except IndexError:
            break
        j += 1
    i += 1

print numOfMax
