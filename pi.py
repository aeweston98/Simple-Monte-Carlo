from __future__ import division
import time
import numpy as np
import matplotlib.pyplot as plt

""" Next Step: Get proper random input stream rather than
pseudorandom numpy RNG"""

#input variable n is the number of iterations the model will use, lower bound of 1000
def estimate_pi(n):

	inside_circle_count = 0;
	total_count = n;

	for i in range(n):
		x = np.random.rand(1)
		y = np.random.rand(1)
		if(x**2 + y**2 <= 1):
			inside_circle_count += 1

	est_pi = 4 * inside_circle_count / total_count
	print("Pi is estimated to be %s with %d iterations." % (str(est_pi), total_count))


for x in (1000, 10000, 100000, 1000000, 10000000, 100000000):
	start_time = time.time()
	estimate_pi(x)
	print("Running Time: %s seconds" % (str(time.time() - start_time)))