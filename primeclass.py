
"""Creating prime class"""
class Prime:

    def __init__(self):
        self.list = []

    """creating a function for prime numbers"""
    def prime(self,range1,range2):
        """An empty list to store the prime number the range1 to range2"""
        arr = []
        for num in range(range1,range2+1):
            if Prime.prime_check(self,num):
                arr.append(num)
        self.list.append(arr)
        return arr

    """Function for printing the 2d array"""
    def Print(self,itr):
        for num in range(itr):
            print(self.list[num])

    """To check number is prime or not"""
    def prime_check(self,num):
        if num < 2:
            return False
        count = 0
        for number in range(2,(num//2)+1):
            if num % number == 0:
                count += 1
                return False
        if count == 0:
            return True

    """crating a function to get the anagram number"""
    def anagram(self, num):
        temp = 0
        while num >= 10:
            temp = (temp * 10) + (num % 10)
            num = num // 10
        temp = (temp * 10) + (num % 10)
        return temp

