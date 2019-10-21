#unit test
#The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.

import sys
import timeit
import functools
	
""" Fibonnaci number """
	
def check_num(num):
    if num<0: 
       print("Incorrect input") 
    elif num == 0:
        return 0
    # First Fibonacci number is 0 
    elif num==1: 
       return 0
    # Second Fibonacci number is 1 
    elif num==2: 
       return 1
    else:
       return num

def fibnumber(n):
    a,b = 0,1
    for i in range(n):
        print("%d  " % a)
        a,b = b, a+b
    print("%d  " % a)
    return 0
	
def fib(n):
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    print("fib = ", fib)
    return fib

"""Recursive function  """
def fibRecursive(n):
   if n <= 1:
       return n
   else:
       return(fibRecursive(n-1) + fibRecursive(n-2))
def callfibRecursive(n):
    for i in range(n+1):
       print(fibRecursive(i))    
    return 0
	
if __name__ == '__main__':
    numero=5
    num=check_num(numero)
    print("Fibonaci for 0 to ",num)
    fibnumber(num)
    fib(num)
    callfibRecursive(num)
    print("Timing...")
    #timeit.timeit(functools.partial(fibnumber, 5))

