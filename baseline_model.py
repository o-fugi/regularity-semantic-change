import random
import matplotlib.pyplot as plt

total_ranks = 10000

diff = []

predicted_rank = list(range(0, total_ranks))
random.shuffle(predicted_rank)

diff = [abs(actual - predicted) for actual, predicted in zip(list(range(0, total_ranks)), predicted_rank)]

plt.xlabel('Difference between actual and predicted')
plt.ylabel('Frequency')
plt.hist(diff, bins=100)
plt.show()
