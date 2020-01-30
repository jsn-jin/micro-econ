
import numpy

M = numpy.zeros((2,2)) 	# initializes M as a 2*2 matrix of zeros
y = numpy.zeros(2);		# initializes y as a length 2 vector

# Fill in the number for M
M[0,0] = 3
M[0,1] = 2
M[1,0] = -1
M[1,1] = 4


# Fill in the numbers for y
y[0] = 5
y[1] = 6

# Solve x = M^-1*y
x = numpy.linalg.solve(M,y)

def main():
	# Print the solution
	print("x1 = %g" % x[0])
	print("x2 = %g" % x[1])
	for i in range(10):
		print(i)
		for j in range(5):
			print(2*j)

	for name in ["Asheley", "Bob", "Charles"]:
		print(name);

main()















