
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Deque:
    def __init__(self):
        self.rear=None
        self.front=None
        self.count=0

    def add_at_front(self,value):
        if self.rear==None:
            self.rear=self.front=value
            self.count+=1
        else:
            value.next=self.front
            self.front=value
            self.count+=1

    def add_at_rear(self,value):
        if self.rear==None:
            self.front=self.rear=value
            self.count+=1
        else:
            self.rear.next=value
            self.rear=value
            self.count+=1

    def remove_front(self):
        if self.rear==None:
            print("Queue is empty !!nothing to remove")
        else:
            if self.front==self.rear:
                node_data=self.front.data
                self.front=self.rear=None
                self.count-=1
                return node_data
            else:
                node_data=self.front.data
                self.front=self.front.next
                self.count-=1
                return node_data

    def remove_from_rear(self):
        if self.rear==None:
            print("Queue is empty !!nothing to remove")
        else:
            if self.front==self.rear:
                node_data=self.front.data
                self.front=self.rear=None
                self.count-=1
                return node_data
            else:
                node_data=self.rear.data
                temp=self.front
                while temp.next!=self.rear:
                    temp=temp.next
                self.rear=temp
                temp.next=None
                self.count-=1
                return node_data

    def is_empty(self):
        if self.rear==None:
            return True
        else:
            return False

    def size(self):
        return self.count

    def traverse(self):
        if self.rear==None:
            print("Queue is empty!!")
        else:
            temp=self.front
            while temp!=None:
                print(temp.data)
                temp=temp.next









