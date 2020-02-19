
"""Add the Prime Numbers that are Anagram in the Range of 0 - 1000
in a Queue using the Linked List and Print the Anagrams from the Queue.
Note no Collection Library can be used.
"""
from queue import Queue, Node
from primeclass import Prime

"""Creating object of queue class"""
obj = Queue()

"""Creating object of prime class"""
prime_obj = Prime()

"""Creating prime_anagram list"""
prime_anagram = []

"""Creating list of prime number in given range"""
prime_list = prime_obj.prime(0,1000)

"""Checking prime number anagran or not"""
for num in prime_list:
    if num <= 10:
        continue
    number = prime_obj.anagram(num)
    if prime_obj.prime_check(number) and 0 <= number <= 1000:
        prime_anagram.append(number)
        prime_anagram.append(num)
        prime_list.remove(number)

"""finding the length of prime anagram list"""
length = len(prime_anagram)

"""Adding the prime anagram in to queue"""
for number in range(length):
    num=Node(prime_anagram[number])
    obj.enqueqe(num)

"""Printind the anagram from queue """
obj.traverse()

