import random
import matplotlib.pyplot as plt

total_ranks = 100

diff = []

for i in range(0, 10000):
	x = random.randrange(total_ranks)
	y = random.randrange(total_ranks)
	diff.append(abs(x-y))


plt.xlabel('Difference between actual and predicted')
plt.ylabel('Frequency')
plt.hist(diff, bins=100)
plt.show()
