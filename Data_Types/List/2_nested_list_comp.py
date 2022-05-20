"""
Nested Lists:
"""
import copy

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Transpose comprehension
matrix_transpose = [[row[i] for row in matrix] for i in range(3)]
print(matrix_transpose)
"""
# Equivalent
transposed = []
for i in range(3):
    transposed.append([row[i] for row in matrix])
print(transposed)
"""
"""
transposed = []
for i in range(3):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)    
"""

# zip() Function
print("Zip To List :", list(zip(*matrix)))


# Comprehension:
new_matrix = [[j for j in range(4)] for i in range(4)]
print(new_matrix)


# Flatten List of Lists:
flatten_matrix = [v for sub in matrix for v in sub]
print("Flatten List :", flatten_matrix)


# Reversing order of inner List in List of Lists:
outputList = []
length = len(matrix)
print("Original List :", matrix)
for i in range(length):
    matrix[length - 1 - i].reverse()
    outputList.append(matrix[length - 1 - i])
print("Reversed List :", outputList)


myList = [[1, 2, 3, 4, 5], [10, 20, 30], [12, 24, 36], [11, 22, 33], [12, 13, 23]]
print("Nested List :", myList)
# Accessing Element:
print("Accessing List Item :", myList[1][2])


# ----Sorting List of Lists: Hacker Rank----
# Using Third element of the inner List:
myList.sort(key=lambda x: x[2])  # or
# outputList = sorted(myList, key=lambda x: x[2])  # Using sorted method
# print(outputList)

# Using Last element of inner List:
# myList.sort(key=lambda x: x[-1])
# Using Length of inner List:
# myList.sort(key=len)
print("Sorted List is:")
print(myList)


# Copy List of Lists...
sh_copy_List = copy.copy(myList)  # Shallow Copy
print(sh_copy_List)

deepcopy_List = copy.deepcopy(myList)  # Deep Copy
print(deepcopy_List)
