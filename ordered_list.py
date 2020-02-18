"""  Ordered_list
 Read a List of Numbers from a file and arrange it ascending Order in a Linked List.
 Take user input for a number,
 if found then pop the number out of the list else insert the number in appropriate position

"""
from linkedlist import Linked_List
from linkedlist import Node

""" creating object for linked list"""

obj=Linked_List()

def main1():

    """ open the file and read the file"""

    file = open( 'file2', 'r')
    lines_of_file = file.readlines()
    for singal in lines_of_file:
        number = singal.lower().split()
        for num in number:
            first = Node(int(num))

            """Adding number into linkedlist into sorted order"""

            obj.sorted_list(first)
    print("The number in the linked list--->")

    """ Printing all the element into the list"""

    obj.traverse()

    """taking input from user to search the number into list"""

    search = int(input("Enter the number to search into list:"))
    if obj.search(search):

        """The searched number is found in list 
        then deleteing the number into the list"""

        obj.delete_word(search)
        print("The number you searched is deleted :")
    else:
        """ The searched number is not found in the list
         then number is to be added to list """

        add_num=Node(search)
        obj.sorted_list(add_num)
        print("The word you searched is added to list!!")
    obj.traverse()

"""calling the function"""

main1()