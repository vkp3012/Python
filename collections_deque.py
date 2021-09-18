"""
collections.deque()

A deque is a double-ended queue. 
It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends 
and pops from either side of the deque with approximately the same  
O(1) performance in either direction.

Example :- 
from collections import deque

d = deque()
d.append(1)
d.appendleft(2)
d.clear()
d.extendleft('432')
d.count('1')
d.pop()
d.popleft()
d.extend('7896')
d.remove("3")
d.reverse()
d.rotate(7)
print(d)

Question:-

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.
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
