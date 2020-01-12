#This script makes functions for basic math operations

#This defines a function that takes two inputs: a and b, and returns a times b  
def multiply(a,b):
    return a * b

#This defines a function that takes two inputs: a and b, and returns a plus b  
def add(a,b):
    return a + b

#This defines a function that takes two inputs: a and b, and returns a minus b  
def subtract(a,b):
    return a - b

#This defines a function that takes two inputs: a and b, and returns a divded by b  
def divide(a,b):
    return a / b

#This defines a function that takes an inputs: a , and returns a squared 
def square(a):
    return a ** 2

#This defines a function that takes an inputs: a , and returns a cubed 
def cube(a):
    return a ** 3

#This defines a function that takes an inputs: a and n, and returns 'a' squared n times.
def square_n(a,n):
    return a ** (2**n)



print("I'm going use the calculator functions to divide 5 and 6")
w = divide(5,6)
print(w)  

print("I'm going use the calculator functions to square 2")
x = square(2)
print(x)  

print("I'm going use the calculator functions to cube 2")
y = cube(2)
print(y) 

print("I'm going use the calculator functions to square 2 three times")
z = square_n(2,3)
print(z) 

