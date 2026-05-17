import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

print(np.argsort(arr))


print(np.argpartition(arr, 3))