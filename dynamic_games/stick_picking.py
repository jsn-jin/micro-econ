import numpy

N = 10

nAmin = 1
nAmax = 3
nBmin = 1
nBmax = 3

pAwin = numpy.zeros(N)
pBwin = numpy.zeros(N)
pAtake = numpy.zeros(N)
pBtake = numpy.zeros(N)

pAwin[0] = 0
pAtake[0] = 1
pBwin[0] = 0
pBtake[0] = 1

for n in range(2,N+1):
    if(n<=nAmin):
        pAwin[n-1] = 0
        pAtake[n-1] = n
    if(n<=nBmin):
        pBwin[n-1] = 0
        pBtake[n-1] = n

    if(n>nAmin):
        found_winning_t = 0
        for t in range (nAmin, nAmax+1):
            remaining_sticks = n-t
            if remaining_sticks>=1 and pBwin[remaining_sticks-1]==0:
                pAwin[n-1] = 1
                pAtake[n-1] = t
                found_winning_t = 1
            if found_winning_t == 0:
                pAwin[n-1] = 0
                pAtake[n-1] = nAmin
    if(n>nBmin):
        found_winning_t = 0
        for t in range (nBmin, nBmax+1):
            remaining_sticks = n-t
            if remaining_sticks>=1 and pAwin[remaining_sticks-1]==0:
                pBwin[n-1] = 1
                pBtake[n-1] = t
                found_winning_t = 1
            if found_winning_t == 0:
                pBwin[n-1] = 0
                pBtake[n-1] = nBmin

for n in range(1,N+1):
    print("n=%d, pAwin=%d, pAtake=%d, pBwin=%d, pBtake=%d" % (n, pAwin[n-1], pAtake[n-1], pBwin[n-1], pBtake[n-1]))
