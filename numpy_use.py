import numpy as np

arr = np.array([20, 35,26, 25, 30])

result = np.where(arr == 26)

if result[0].size > 0:
    print("Element found at index:", result[0][0])
else:
    print("Element not found")