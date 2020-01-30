'''	Cournot Competion: Linear Demand / Heterogeneous Firms (cost functions)
	(Data stored in data.txt. For more information about the data, refer
	to the file data_cmt.txt)
'''
import numpy

# Read the data from file data.txt
data = open('data.txt','r')

# get the number of firms (n)
# note that n is an integer
# strip: remove the new line character (since there are 2 char(s) in a line)
n = int(data.readline().strip())

# get n lines of ci
# note that c/d/a/b are of type float
c = numpy.zeros(n)
for i in range(n):
    c[i] = float(data.readline().strip())

# get n lines of di
d = numpy.zeros(n)
for i in range(n):
    d[i] = float(data.readline().strip())

# get a from the next line
a = float(data.readline().strip())

# get b from the next (last) line
b = float(data.readline().strip())

data.close()

# initialize matrix M
M = numpy.zeros((n,n))
for i in range(n):
    for j in range(n):
        if(i == j):
            M[i,j] = 2 * b + 2 * d[i]
        else:
            M[i,j] = b

# initialize matrix y          
y = numpy.zeros(n)
for i in range(n):
    y[i] = a - c[i]

q = numpy.linalg.solve(M,y)

print(q)