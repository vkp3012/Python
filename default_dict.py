"""
Defaultdict()

The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference is 
that a defaultdict will have a default value if that key has not been set yet. 
If you didn't use a defaultdict you'd have to check to see if that key exists, 
and if it doesn't, set it to what you want.


-----------------------------------------------------
d = defaultdict(list)
d['python'].append("awesome")
d['Something-else'].append('not relevant')
d['python'].append("langauge")
for i in d.items():
    print(i)
"""

from collections import defaultdict

# input
#-----------------------
n,m = map(int,input().split(" "))

# Let's get the groups of list
#--------------
#input1 = ['a','a','b','a','b']
#input2 = ['a','b']

input1 = list()
for i in range(n):
    input1.append(input())

    input2 = list()
for i in range(m):
    input2.append(input())

# Calculate Output
#-----------------

d = defaultdict(list)

# Fill d with input1 value
for i in range(n):
    d[input1[i]].append(i+1)

# Appling the logic Printing
for i in input2:
    if i in d:
        print(*d[i])
    else:
        print(-1)