import numpy as np

# Creating Numpy Array:
arr = np.array([1, 2, 3])
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

arr = np.array((1, 3, 2))
print(arr)

# Accessing Array Index:
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array:\n", arr)
print("Type :", type(arr))
print("No. of Dimensions :", arr.ndim)
print("Shape :", arr.shape)
print("Size :", arr.size)  # Total No. of elements
print("Element Type :", arr.dtype)

sliced_arr = arr[:2, ::2]
print("Array with first 2 rows and alternate columns(0 and 2):\n", sliced_arr)

Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print("Elements at indices (1, 3), (1, 2), (0, 1), (3, 0):\n", Index_arr)

# Basic Array Operations:
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[4, 3],
              [2, 1]])

print("Adding 1 to every element:", a + 1)
print("Subtracting 2 from each element:", b - 2)
print("Sum of all array elements: ", a.sum())
print("Array sum:\n", a + b)

# Data Type in Numpy:
x = np.array([1, 2])
print("Integer Data Type :", x.dtype)
x = np.array([1, 2], dtype=np.int64)
print("Forcing Data Type :", x.dtype)

# Math operations on DataType Array:
arr1 = np.array([[4, 7], [2, 6]], dtype=np.float64)
arr2 = np.array([[3, 6], [2, 8]], dtype=np.float64)

print("Addition of Two Arrays:", np.add(arr1, arr2))
print("Addition Array elements:", np.sum(arr1))
print("Square root of Array elements:", np.sqrt(arr1))
print("Transpose:", arr1.T)



