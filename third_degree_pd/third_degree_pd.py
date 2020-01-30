import numpy

# Open the data file for reading
myfile = open('data.txt','r')

# First line is n
# strip means stripping the linebreak
# int means converting characters to numbers
n = int(myfile.readline().strip())

# Next n lines are a
# Float is a numerical data
a = numpy.zeros(n)
for i in range(n):
    a[i] = float(myfile.readline().strip())

# Next n lines are b
b = numpy.zeros(n)
for i in range(n):
    b[i] = float(myfile.readline().strip())

# Next line is c
c = float(myfile.readline().strip())

# Next line is d
d = float(myfile.readline().strip())

myfile.close()

# Initialize M
M = numpy.zeros((n,n))
for i in range(n):
    for j in range(n):
        if(i == j):
            M[i,j] = 2 * b[i] + 2 * d
        else:
            M[i,j] = 2 * d

# Initialize Y            
y = numpy.zeros(n)
for i in range(n):
    y[i] = a[i] - c

# Solve the equation
q = numpy.linalg.solve(M,y)

#Solve for prices
p = numpy.zeros(n)
for i in range(n):
    p[i] = a[i] - b[i] * q[i]

print(p)
