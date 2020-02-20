"""Calculating total number of binary search tree with number of nodes"""

while True:
    try:
        number_of_nodes=int(input(("Enter the number of nodes :")))
        if number_of_nodes > 0:
            break
        else:
            print("Invalid input !!")
    except ValueError:
        print("Invalid input!!")

"""Defining function for calculating factorial of number"""
def factorial(number):
    fact=1
    while number>0:
        fact=fact*number
        number-=1
    return fact

"""Calculating number of binary search tree"""
def number_of_Bst(node):
    """calculating by Catalan Number"""
    a=factorial(2*node)
    b=factorial(node+1)
    c=factorial(node)
    total_num_of_bst=a//(b*c)
    return total_num_of_bst

"""Printing total number of binary search trees"""
print(f"Total number of binary search tree are :{number_of_Bst(number_of_nodes)}")
