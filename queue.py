class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def enqueqe(self,value):
        if self.rear==None:
            self.front=self.rear=value
            self.count+=1
        else:
            self.rear.next =value
            self.rear = value
            self.count += 1

    def dequeue(self):
        if Queue.is_empty(self):
            print("Queue is empty nothing to dequeue!!")
        else:
            if self.front.next==None:
                self.front=None
            else:
                self.front=self.front.next
            self.count-=1

    def is_empty(self):
        if self.rear==None:
            return True
        return False

    def size(self):
        if self.count <= 0:
            print("queue is empty!!")
        print(f"The size of queue is {self.count}")

    def traverse(self):
        if self.count==0:
            print("Queue is empty !!")
        else:
            temp=self.front
            while temp!=None:
                print(temp.data)
                temp=temp.next









