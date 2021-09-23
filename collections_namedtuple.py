"""
collections.namedtuple()

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
"""

from collections import namedtuple
"""
point = namedtuple("point",'x,y')
pt1 = point(1,2)
pt2 = point(3,4)
dot_product = (pt1.x*pt2.x) + (pt1.y*pt2.y)
print(dot_product)
"""
car = nametuple("Car","Price Mileage Colour Class")
xyz = car(Price=10000,Mileage=30,Colour = 'Cyan' ,Class='Y')
print(xyz)
