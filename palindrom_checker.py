
"""
A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam.
We would like to construct an algorithm to input a string of characters and check whether it is a palindrome.

"""

from deque import Deque
from deque import Node

"""Creating object for Deque class"""
obj=Deque()

"""Reading a string from the user"""

string=input(" Enter a string to check wheather it's palindrom or not :")

"""Define a method to check the string is palindrom or not"""

def palindrom_checker(string):
    """Inserting all the character of string into the deque"""
    for character in string:
        ch = Node(character)
        obj.add_at_rear(ch)

    """finding the length of deque"""
    length = obj.size()

    """Creating another string to compare strings"""
    string2 = ""

    """Adding chracters into new string"""
    for len in range(length):
        ch = obj.remove_from_rear()
        string2 += ch

    """Comparing the string and printing is palindom or not"""
    if string == string2:
        print("The string is palindrom!!")
    else:
        print("The string is not palindrom!!")

"""Calling the function by passing string as a argument"""
palindrom_checker(string)




