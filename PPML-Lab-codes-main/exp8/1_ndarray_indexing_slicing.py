import numpy as np

# Creating ndarray object
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# Indexing
print("First element:", arr[0])
print("Third element:", arr[2])

# Slicing
print("First three elements:", arr[0:3])
print("Last three elements:", arr[2:5])
print("Alternate elements:", arr[::2])