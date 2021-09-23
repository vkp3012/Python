"""
collections.namedtuple()

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
"""

from collections import namedtuple
"""
-------------------------------------------------------------
point = namedtuple("point",'x,y')
pt1 = point(1,2)
pt2 = point(3,4)
dot_product = (pt1.x*pt2.x) + (pt1.y*pt2.y)
print(dot_product)
----------------------------------------------------------------
----------------------------------------------------------------
car = namedtuple("Car","Price Mileage Colour Class")
xyz = car(Price=10000,Mileage=30,Colour = 'Cyan' ,Class='Y')
#print(xyz)
print(xyz.Class)
--------------------------------
"""

N = int(input())
fields = input().split()
total = 0
for i in range(N):
    students = namedtuple('student',fields)
    field1,field2,field3,field4 = input().split()
    student = students(field1,field2,field3,field4)
    total += int(student.MARKS)
print('{:.2f}'.format(total/N))




"""
Defaultdict()

The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference is 
that a defaultdict will have a default value if that key has not been set yet. 
If you didn't use a defaultdict you'd have to check to see if that key exists, 
and if it doesn't, set it to what you want.
"""

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['Something-else'].append('not relevant')
d['python'].append("langauge")
for i in d.items():
    print(i)