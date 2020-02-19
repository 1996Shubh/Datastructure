
from primeclass import Prime

print("Prime number in range  0 to 1000 is :")

"""Creating object for prime class"""
obj = Prime()

"""Declare a iterator variable to count the loop iterations"""
itr = 0
"""Creating an empty list for strong the primes """
arr = []
for number in range(0,1000,100):
    """Calling the prime function to get the prime numbers"""
    arry = obj.prime(number, number+100)
    itr +=1
    arr.append(arry)
"""Calling the function to print all numbers in 2D array"""
obj.Print(itr)