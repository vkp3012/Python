
"""
Input Format

The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.

--------------------------------------------------------------------------
Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

----------------------------------------------------
Sample Output

8
---------------------------------------------------------------------------------
k = int(input())
arr = list(map(int,input().split()))

myarr = set(arr)
#print (myarr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
"""

k = int(input())
d = map(int,input().split())
s1 = set()
s2 = set()
for i in d:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)

s3 = s1.difference(s2)
print(s3.pop())

"""
Explanation

The list of room numbers contains 31 elements. Since K is 5, 
there must be 6 groups of families. 
In the given list, all of the numbers repeat 5 times except for room number 8.
Hence, 8 is the Captain's room number.
"""