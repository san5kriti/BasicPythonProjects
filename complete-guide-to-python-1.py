# Complete Introduction to Python 

# 1. Strings & Printing them.
print("Hello World")  # Print a simple string
print("Hey world")    # Print another simple string

a = 5
print(a)              # Print the integer value of variable 'a'

# 2. Basic Arithmetic.
num1 = 10
num2 = 5

print(num1 + num2)   # Addition: 15
print(num1 - num2)   # Subtraction: 5
print(num1 * num2)   # Multiplication: 50
print(num1 / num2)   # Division: 2.0
print(num1 ** num2)  # Power: 100000

# You can also import the module 'math' for more advanced operations
import math

print(math.sqrt(num1))  # Square root: 3.1622776601683795
print(math.factorial(num2))  # Factorial: 120
print(math.gcd(num1, num2))  # Greatest common divisor: 5

# 3. Variables and Data Types
integer_var = 42            # Integer
float_var = 3.14            # Float
string_var = "Hello, Python!" # String
boolean_var = True          # Boolean

print(type(integer_var))    # Output: <class 'int'>
print(type(float_var))      # Output: <class 'float'>
print(type(string_var))     # Output: <class 'str'>
print(type(boolean_var))    # Output: <class 'bool'>

# 4. Logical Operations
a = True
b = False

print(a and b)  # Logical AND: False
print(a or b)   # Logical OR: True
print(not a)    # Logical NOT: False

# 5. Assignment Operations
x = 10
x += 5  # x = x + 5
print(x)  # Output: 15

x -= 3  # x = x - 3
print(x)  # Output: 12

x *= 2  # x = x * 2
print(x)  # Output: 24

x /= 4  # x = x / 4
print(x)  # Output: 6.0

# 6. Functions (Lambda, def, higher-order functions)
# Function using def
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Lambda function
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Higher-order function
def apply_function(f, x):
    return f(x)

print(apply_function(square, 5))  # Output: 25

# 7. If Else
number = 7

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 8. Lists & Arrays
# List in Python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Array (using numpy)
import numpy as np
array = np.array([1, 2, 3, 4])
print(array)  # Output: [1 2 3 4]

# 9. List Slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])  # Output: [3, 4, 5]
print(numbers[:3])   # Output: [1, 2, 3]
print(numbers[6:])   # Output: [7, 8, 9, 10]

# 10. File Handling
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, file handling!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Hello, file handling!

# 11. Importing Libraries
import math  # Importing the math module

print(math.pi)  # Output: 3.141592653589793
print(math.log(10))  # Output: 2.302585092994046

# 12. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful.")
finally:
    print("Execution completed.")

# 13. Object-Oriented Programming
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_age(self):
        return self.age

# Creating an object of the Dog class
dog = Dog("Buddy", 5)
print(dog.bark())  # Output: Buddy says Woof!
print(dog.get_age())  # Output: 5
