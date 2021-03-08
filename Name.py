import numpy as np


def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype:%s'
          % (a.ndim, a.shape, a.dtype))


a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(a)
print(print_array_details(a))
a = a.reshape([2, 4])
print(a)

print(print_array_details(a))

a = a.reshape([2, 2, 2])

print(a)

print(print_array_details(a))
