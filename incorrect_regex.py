"""
You are given a string S.
Your task is to find out 
whether S is a valid regex or not.

Input: ------------
The first line contains integer T , the number of test cases.
The next T lines contains the string S.
"""
import re

"""
for _ in range(int(input().split())):
    try:
        re.match(input(),"")
        print("True")
    except:
        print("False")

"""

n = input()

for i in range(int(n)):
    key = input()
    try:
        re.compile(key)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)




