"""
Take an Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
where parentheses are used to order the performance of operations.
Ensure parentheses must appear in a balanced fashion.

"""

from stack import Stack
from stack import Node

"""Creating object for stavk class"""
obj=Stack()

"""input from user"""
expression=input("Enter any expression :")

"""Function definition"""
def balanced_parentheses(expression):
    open_parentheses="({["
    closed_parentheses=")}]"

    for brackets in expression:
        if brackets in open_parentheses:
            bracts=Node(brackets)
            obj.push(bracts)
        elif brackets in closed_parentheses:
            obj.pop()

    if obj.is_empty():
        print("Given expression is balanced!!")
    else:
        print("Given expression is Not balanced!!")

"""Function calling"""
balanced_parentheses(expression)


