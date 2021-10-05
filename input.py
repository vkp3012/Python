"""
input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).
-------------------------------------------------------------------------------
Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'

--------------------------------------------------------------------------------
Task

You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x)=k.

----------------------------------------------
Constraints
All coefficients of polynomial P are integers.
x and y are also integers.

-------------------------------------------------------------------------------------
Input Format

The first line contains the space separated values of x and k.
The second line contains the polynomial P.
"""

x,k = map(int,input().split())
print(k==eval(input()))

"""
ui = input().split()
x = int(ui[0])
print(eval(input())==int(ui[1]))
"""