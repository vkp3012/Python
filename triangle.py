"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

------------------------------------------------------------------------
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)*i)

------------------------------------------------------------------------
Output:- 


1
22
333
4444
55555
"""
for x in range(1,int(input())+1):
    print(((10**x-1)//9)**2)