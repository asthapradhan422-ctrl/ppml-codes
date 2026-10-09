import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Saving array
np.save("myarray.npy", arr)

print("Array saved successfully.")

# Loading array
new_arr = np.load("myarray.npy")

print("Loaded array:", new_arr)