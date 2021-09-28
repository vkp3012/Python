
"""
# Find Fibonacci Number Series from

def fibonacci(n):
    list = [0,1]
    for x in range(2,n):
        list.append(list[x-2]+list[x-1])
    return(list[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(fibonacci(n)))

"""

"""
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 
0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and 
print the list.

-----------------------------------------------------------------------------------------------
Concept : -

The map() function applies a function to every member of an iterable and returns the result. 
It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length of each name.

--------------------------------------------------------------------------------------------------------------------------

print(list(map(len, ['Tina', 'Raj', 'Tom'])))
[4, 3, 3]

"""

# A list on a single line containing the cubes of the first N fibonacci numbers.

cube = lambda x : pow(x,3)

def fibonacci(n):
    list = [0,1]
    for x in range(2,n):
        list.append(list[x-2]+list[x-1])
    return(list[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube,fibonacci(n))))
    
"""

# Find The Fibonacci Number
def fibonacci(n):
    list = [0,1]
    for x in range(2,n):
        list.append(list[x-2]+list[x-1])
    return(list[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(fibonacci(n)))
"""