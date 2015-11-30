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
#searching through all of the entries
maximum = Grid[0][0]
numOfMax = 0
for i in range(len(Grid)):
    for j in range(len(Grid[i])):
        if Grid[i][j] == maximum:
            numOfMax += 1
        else:
            break

print numOfMax
