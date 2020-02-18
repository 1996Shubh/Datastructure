""" Creating the node class"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

""" Creating the stack class"""
class Stack:
    def __init__(self):
        self.top=None
        self.count=0

    """ Adding the item into the top of the stack"""
    def push(self,value):
        if self.top==None:
            self.top=value
            self.count+=1
        else:
            value.next=self.top
            self.top=value
            self.count+=1

    """ Remove the top item from stack"""
    def pop(self):
        if self.top==None:
            print("Stack is empty!!")
        else:
            if self.top.next==None:
                self.top=None
                self.count-=1
            else:
                self.top=self.top.next
                self.count-=1

    """ Return the top parameter from the stack"""
    def peek(self):
        if self.top==None:
            return "Stack is empty"
        else:
            return self.top.data

    """ Checking the stack is empty or Not"""
    def is_empty(self):
        if self.top==None:
            return True
        else:
            return False

    """Return size of the stack"""
    def size(self):
        return self.count




