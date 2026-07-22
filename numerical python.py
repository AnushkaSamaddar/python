import numpy as np
arr=np.array([1,2,3,4])
arr2=np.array([[[1,2,3],
                [4,5,6],
                [7,8,9]]])
print(arr)
print(type(arr))
print(arr2)
print(arr2.ndim)
print(arr.ndim)
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
print(arr.dtype)