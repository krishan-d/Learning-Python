from collections import deque

newList = [10, 30, -40, 77]
queue = deque(newList)
print(queue)

queue.append(-26)
print(queue)

queue.popleft()
queue.popleft()
print(queue)
