"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:


"""
for x in range(1,int(input())+1):
    print(((10**x-1)//9)**2)