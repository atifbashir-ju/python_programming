class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num
n = number(5)
m = number(10)
print(n + m.n)  

#operators in python can be overloaded using the following methods:

# p1+p2  # __add__
# p1-p2  # __sub__            
# p1*p2  # __mul__
# p1/p2  # __truediv__
# p1//p2 # __floordiv__
# p1%p2  # __mod__


