import math

def display_options():
    print("Hello User, this is a calculator made by Python!")
    print("The following operations are available: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Logarithm (log)")

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y 

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero."

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else: 
        return "Error: Invalid input for logarithm."

def calculator(): 
    while True: 
        display_options()
        option = input("Enter the symbol of a mathematical operation or 'q' to quit: ")

        if option == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))

        if option != 'log':
            num2 = float(input("Enter the second number: "))

        if option == '+': 
            result = addition(num1, num2)
        elif option == '-':
            result = subtraction(num1, num2)
        elif option == '*':
            result = multiplication(num1, num2)
        elif option == '/':
            result = division(num1, num2)
        elif option == '^': 
            result = power(num1, num2)
        elif option == '%':
            result = modulus(num1, num2)
        elif option == 'log':
            base = float(input("Enter the base for the logarithm: "))
            result = logarithm(num1, base)
        else:
            result = "Invalid input"

        print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
