import math

def prime(n):
    if n < 2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if i % n == 0:
            return False
    return True

prime(5)