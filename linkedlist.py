"""
--------Linked list--------
"""
""" Creating Node class """
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

""" Creating Linkedlist class"""
class Linked_List:
    def __init__(self):
        self.head=None

    """Inserting the element into Linledlist"""
    def insert(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next==None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    """Inserting element at beginning of Linkedlist"""
    def insert_first(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    """ Inserting element at a position"""
    def insert_at_mid(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            position=int(input("Enter the position at you want to input:"))
            while True:
                if position > Linked_List.len(self) :
                    print("You enterd wrong position :")
                    position = int(input("Enter the position at you want to input:"))

                else:
                    number = 1
                    lastnode = self.head
                    llastnode = lastnode.next
                    if position == 1:
                        Linked_List.insert_first(self,newnode)
                        break;
                    else:
                        while number < position-1:
                            lastnode = lastnode.next
                            llastnode = lastnode.next
                            number += 1
                        newnode.next = llastnode
                        lastnode.next = newnode
                        break
    """ Searching element into Linkedlist"""
    def search(self,newnode):
        if self.head==None:
            print("Nothing to search !! List is empty")
        else:
            lastnode=self.head
            while lastnode!=None:
                if newnode==lastnode.data:
                    print("The word is found in the list!!")
                    return 1
                else:
                    lastnode=lastnode.next
            if lastnode==None:
                print("The word is not found into list!!")
                return 0

    """Delete element from last in Linkedlsit"""
    def delete(self):
        if self.head==None:
            print("List is empty!!Nothing to dalete")
        else:
            lastnode=self.head
            llastnode=lastnode.next
            while llastnode.next!=None:
                lastnode=llastnode
                llastnode=llastnode.next
            lastnode.next=None
            llastnode.data=None

    """ Delete a word from that position"""
    def delete_word(self, value):
        if self.head == None:
            print("List is empty !!Nothing to delete")
        else:
            if self.head.data == value:
                self.head = self.head.next
            else:
                temp1 = self.head
                temp = self.head.next
                while temp!=None:
                    if temp.data == value:
                        temp1.next = temp.next
                        break
                    temp1 = temp1.next
                    temp = temp.next
                if temp is None:
                    print("Element not found")

    """Finding length of Linkedlist"""
    def len(self):
        length=0
        lastnode=self.head
        while lastnode!=None:
            lastnode=lastnode.next
            length+=1
        return length

    """Traverseing all the element from Linkedlist"""
    def traverse(self):
        if self.head==None:
            print("List is empty:")
            return
        currentnode=self.head
        while True:
            if currentnode==None:
                break
            print(currentnode.data)
            currentnode=currentnode.next

    """Returning the data at given position"""
    def index(self,position):
        length=Linked_List.len(self)
        if position < 0 and position > length:
            print("Invalid input!!")
        else:
            temp=self.head
            count=1
            while count<position:
                temp=temp.next
                count+=1
            return temp.data

    """Sorting the Linkedlist"""
    def sorted_list(self, value):
        if self.head == None:
            self.head = value
        else:
            temp=self.head
            if temp.data > value.data:
                value.next = temp
                self.head = value
            else:
                temp2=temp.next
                while temp.next!=None:
                    if (temp2.data > value.data):
                        break
                    temp=temp.next
                    temp2=temp.next
                value.next=temp2
                temp.next=value



