"""
collections.deque()

A deque is a double-ended queue. 
It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends 
and pops from either side of the deque with approximately the same  
O(1) performance in either direction.
"""



from collections import deque
d = deque()
for i in range(int(input())):
    c = input().split()
    if c[0] == "append":
        d.append(c[1])
    elif c[0] == "appendleft":
        d.append(c[1])
    elif c[0] == "pop":
        d.pop()
    elif c[0] == "popleft":
        d.popleft()

print(*d)
