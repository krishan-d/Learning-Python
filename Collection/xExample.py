"""
k Largest/ Smallest Element:
"""

# Using sorting:
# Sort the elements in descending order in O(n*log(n))
# Print the first k numbers of the sorted array O(k).
# Time complexity: O(n*log(n))


def kLargest(array, num):
    array.sort(reverse=True)
    for i in range(num):
        print(array[i], end=" ")


a = [1, 23, 12, 9, 30, 2, 50]
k = 3
kLargest(a, k)


# Using Max Heap:
# Build a Max Heap tree in O(n)
# Use Extract Max k times to get k maximum elements from the Max Heap O(k*log(n))
# Time complexity: O(n + k*log(n))

# using order statistics:
# Use an order statistic algorithm to find kth largest element. O(n)
# Use QuickSort Partition algorithm to partition around the kth largest number O(n).
# Sort the k-1 elements (elements greater than the kth largest element) O(k*log(k))=
# -This step is needed only if the sorted output is required.
# Time complexity: O(n) if we don’t need the sorted output, otherwise O(n+k*log(k))


# Using Min Heap:
# 1.Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k*log(k))
# 2.For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
# - If the element is greater than the root then make it root and call heapify for MH. Else ignore it.
# is O((n-k)*log(k))
# Finally, MH has k largest elements, and the root of the MH is the kth largest element.

def FirstKElements(array, size, k):
    # Creating Min Heap for given array with only k elements.
    minHeap = []
    for i in range(k):
        minHeap.append(array[i])

    # Loop For each element in array after the kth element.
    for i in range(k, size):
        minHeap.sort()

        # If current element is smaller than minimum ((top element of the minHeap) element,
        # do nothing and continue to next element
        if minHeap[0] > array[i]:
            continue

        # Otherwise, Change minimum element (top element of the minHeap) to current element
        # by polling out the top element of the minHeap
        else:
            minHeap.pop(0)
            minHeap.append(array[i])

    # Now min heap contains k maximum elements
    for i in minHeap:
        print(i, end=" ")


a = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
size = len(a)
k = 3  # Size of Min Heap
FirstKElements(a, size, k)
