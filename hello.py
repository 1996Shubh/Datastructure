# print("hello")

# class People:
#     def __init__(self,first,last,age):
#         self.first=first
#         self.last=last
#         self.age=age
#
# p1=People('shubham','agarwal',23)
# print(p1.first)

# class People:
#     def __init__(self,first,last,age):
#         self.first=first
#         self.last=last
#         self.age=age
#
#     def full_name(self):
#         return f"{self.first} {self.last}"
#
#     def is_above_18(self):
#         return self.age>18
#
# p1=People("shubham",'kumar',18)
# print(People.is_above_18(p1))

# class Laptop:
#     def __init__(self,brand,processer,price):
#         self.brand=brand
#         self.processer=processer
#         self.price=price
#
#     def apply_discount(self,discount):
#         dis=(discount/100)*self.price
#         return self.price-dis
#
#
# laptop1=Laptop('Asus',"i5_processer",45500)
# print(laptop1.apply_discount(40))

# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#
#     def area(self,radius):
#         return Circle.pi*self.radius*self.radius
#     def circumference(self):
#         return 2*Circle.pi*self.radius
#
# p1=Circle(4)
# print(p1.circumference())

# def Binary(a,n,key):
#     l=0
#     r=n
#     while(l<r):
#         mid=(l+r)//2
#         if key==a[mid]:
#             return mid
#         elif(key<a[mid]):
#             r=mid-1
#         else:
#             l=mid+1
#     return -1
#
# # f=open("List.txt",'r')
# # data = f.readline()
# # l=[i.strip() for i in data.split(',')]
#
# l=['apple','orange','graps','banana','kiwi']
# data=sorted(l)
# print(data)
# key=input("enter name:")
# print(key)
# pos=Binary(data,len(data),key)
# if pos==-1:
#     print("Element not present in array")
# else:
#     print("Element found at position ",pos)
# # f.close()

# class computer:
#     def __init__(self,processer,ram):
#         self.proces=processer
#         self.ram=ram
#         print("shubh")
#     def config(self):
#         print(f"hello {self.proces} {self.ram}")
#
# comp1=computer('i5','16gb')
# comp1.config()


# class car:
#     school='Telusko'
#
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     def get_m1(self):
#         return self.m1
#
#     def set_m2(self,value):
#         self.m2=value
#
# s1=student(89,85,99)
# s2=student(88,98,87)

# class A:
#     def __init__(self):
#         print("INit")
#     def feature1(self):
#         print("feature1 is working:")
#     def feature1(self):
#         print("feature2 is working:")
# class B:
#     def __init__(self):
#         super().__init__() #it will also call init of a also
#         print("INit in B")
#     def feature3(self):
#         print("feature3 is working:")
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print("Init in c")


# a1=C()
# print(a1.feature1())
#class method as a constructor
# class Person:
#     count_instance=0#class variable / class attribute
#     def __init__(self,first,last,age):
#         Person.count_instance+=1
#         self.first=first
#         self.last=last
#         self.age=age
#
#     # class method as a constructor
#     @classmethod
#     def from_string(cls,string):
#         first,last,age=string.split(',')
#         return cls(first,last,age)
#
#     @staticmethod
#     def hello():
#         print("hello static method called")
#
#     @classmethod
#     def count_instances(cls):
#         return f"you have created {cls.count_instance}"
#
#     def full_name(self):
#         return f"{self.first} {self.last}"
#
#
# s1=Person("shubham",'kumar',23)
# print(s1.full_name())
# print(Person.count_instances())
#
# p3=Person.from_string('shubham ,agarwal,23')
# print(p3.full_name())
# Person.hello()


# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         self.price=price
#
#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}......")
#
#     def full_name(self):
#         return f"{self.brand} {self.model_name} {self.price}"
#
#     def send_message(self):
#         pass
#     # @property #for using as a attribute
#     # def complete_specification(self):
#     #     return f"{self.brand} {self.model_name} and price is{self.price}"
#     # #getter() #setter()
#     # @property
#     # def price(self):
#     #     return self.price
#     #
#     # @price.setter
#     # def price(self):
#     #     self.price=max(price,0)
# class Smartphone(Phone):
#     def __init__(self, brand, model_name,price,ram, internal_memory, rear_camera):
#         # Phone.__init__(self,brand,model_name,price)
#         super().__init__(brand, model_name, price)
#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_camera=rear_camera
#
#
# # phone1=Phone('nokia','x2',16890)
# # print(phone1.__price)
# # print(phone1.__dict__)
# # l=[1,5,7,9]
# # print(sorted(l))
# # x=l.sort()
# # print(l)
#
# # _name --->convection of private name
# # __name__--->dunder/magic method
#
# # print(phone1.complete_specification)
# # phone1.price=-500
# # print(phone1.price)
#
# phone=Phone('nokia','1100',1000)
# smartphone=Smartphone('oneplus','5',30000,'6gb','64gb','20mp')
# print(smartphone.full_name())


# p1=open("test",'r')
# # print(p1.read())
# p2=open("test2",'w')
# for data in p1:
#     p2.write(data)
# p2=open('test2','r')
# print(p2.read())
# # print(p2.read())

#unorderd linked list
# first=Node("shubham")
# second=Node("shivam")
# obj.insert(first)
# obj.insert(second)
# obj.traverse()

# li=[4,5,6]
# for i in li:
#     first=Node(i)
#     obj.insert(first)
#
# obj.traverse()


# def InsertOrder(self, num):
#     # creating a node
#     node = Node.Node(num)
#     node.data = num
#     node.next = None
#     # if head is None it means the list is empty
#     # the first element is to be head
#     sh = self.head
#     if self.head == None:
#         self.head = node
#     else:
#         # Checking that the given data is lessthan head
#         # if yes add the element at 1st and make it as head
#         sh = self.head
#         if node.data < sh.data:
#             self.head = node
#             node.next = sh.next
#         else:
#             # Traversing upto that getting a element greater than or equal to the element
#             # after that inserting the element
#             while sh.next != None:
#                 if sh.data <= node.data and node.data <= sh.next.data:
#                     temp = sh.next
#                     sh.next = node
#                     node.next = temp
#                     return
#                 sh = sh.next
#             # if Traversing reached Last
#             # comparing the new_element with last element and inserting
#             if sh.data > node.data:
#                 temp = sh.next
#                 sh.next = node
#                 node.next = temp
#                 return
#             else:
#                 Linkedlist.add(self, num)
#
#
# #-------------------------------------------------------------------------
#  def sorted_list(self,value):
#         if self.head==None:
#             self.head=value
#         else:
#             # length=Linked_List.len(self)
#             temp=1
#             xx=Linked_List.index(self,temp)
#             if value.data < xx:
#                     Linked_List.insert_first(self,value)
#             else:
#                 while value > xx:
#                     temp+=1
#                     xx=Linked_List.index(self,temp)
#             Linked_List.insert_at_mid(self,value,temp)
#
# #-------------------------------------------------------------------
#     def sorted_list(self,value):
#         if self.head==None:
#             self.head=value
#         else:
#             temp=self.head
#             if temp.data > value:
#                 value.next=temp
#                 self.head=value
#             else:
#                 while temp.data < value:
#                     temp=temp.next


# for character in string:
#     ch=Node(character)
#     obj.add_at_rear(ch)
#
# length=obj.size()
# string2=""
#
# for len in range(length):
#     ch=obj.remove_from_rear()
#     string2+=ch
#
# if string==string2:
#     print("The string is palindrom!!")
# else:
#     print("The string is not palindrom!!")


#------------------------------------------------------------------------------------------------------------------

# def check_parenthesis_balance(self, expression):
#     open_parenthesis = "([{"
#     close_parenthesis = ")]}"
#
#     balance = True
#
#     for bracket in expression:
#
#         print(bracket)
#         if bracket in "([{":
#             self.push(bracket)
#         elif bracket in close_parenthesis:
#             self.pop()
#             # if self.is_empty():
#             #     balance = False
#             #     break
#
#     if self.is_empty():
#         print(f"The inputted expression : {expression}  is balanced")
#     else:
#         print(f"The inputted expression : {expression} is not balanced")


#---------------------------------------------------------------------------------------------------------------------
import json























