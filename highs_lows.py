import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
squares = [1, 2, 3, 4, 45]
input_values = ["pig1", "pig2", "pig3", "pig4", "pig5"]
plt.plot(input_values, squares, linewidth=5)
plt.title('ssquare numbers', fontsize=14)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)
plt.tick_params(axis='bot                                                h', labelsize=14)
plt.show()

