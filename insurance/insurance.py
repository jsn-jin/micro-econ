import numpy

# Set the seed for the random number generator
# This allows for reproducible results
numpy.random.seed(10)

# Number of simulations to perform
R = 5000

# Parameters
gamma = 0.1
w0 = 100
theta = 0.1
mu = numpy.log(10)  # the natural log
sig = 0.1
D = 0.5

# calculated expected utility with and without insurance
# also calculate expected payment by the insurer

EU_noins = 0
EU_ins = 0
Epay = 0

for r in range(R):  # repeat this thing R times

	# Accident or no?
	# Simulate a uniform random variable u(0,1)
	# Accident if u<theta
	
	u = numpy.random.uniform()
	if u < theta:
		accident=1
	else:
		accident=0
		
	# if no accident, wealth is w0 
	if accident==0:
		wealth_noins = w0
		wealth_ins = w0
		payment = 0
	
	# if accident, simulate the loss and the resulting wealth
	if accident==1:
		L = numpy.exp( numpy.random.normal( mu, sig))
		
		# with no insurance, wealth is w0 - L
		wealth_noins = w0 - L
		
		# with insurance, wealth is w0 - L if L is less than D, but D otherwise
		if L<D:
			wealth_ins = w0 - L
			payment = 0
		else:
			wealth_ins = w0 - D
			payment = L - D
			
	# Utilities
	u_noins = -numpy.exp(-gamma*wealth_noins)
	u_ins = -numpy.exp(-gamma*wealth_ins)
	
	# Add to the average
	EU_noins = EU_noins + (1/R)*u_noins
	EU_ins = EU_ins + (1/R)*u_ins
	Epay = Epay + (1/R)*payment
	

# Calculate certainty equivalents
CE_noins = -(1/gamma)*numpy.log(-EU_noins)
CE_ins = -(1/gamma)*numpy.log(-EU_ins)

# Willingness to pay
WTP = CE_ins - CE_noins

# Expected payment by the insurer = actuarially fair premium
fairprem = Epay

# Print the results
print('CE (no insurance) = %g' % CE_noins)
print('CE (insurance) = %g' % CE_ins)
print('WTP for insurance = %g' % WTP)
print('Actuarially fair premium = %g' % fairprem)






