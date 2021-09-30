"""
collections.Counter()

A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

--------------------------------------------------------------------------------------
Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

---------------------------------------------------------------------
Task

Vivek is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Vivek earned.

-------------------------------------------------------------------------

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the Shoe size desired by the customer and , the price of the shoe.
"""

import collections

no_of_shoes = int(input())
shoes = collections.Counter(map(int,input().split()))
customers = int(input())

income = 0 
for i in range(customers):
    size,price = map(int,input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)
