#1
def print_natural_numbers():
    for i in range(1, 11):
        print(i)
print_natural_numbers()
#2
def sum_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter N: "))
print("Sum =", sum_natural_numbers(n))
#3
def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))
#4
def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count
#5
num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))

def is_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return original == rev
#6
num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
#7
def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)
#8
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
#9
choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    print("Result =", divide(num1, num2))
else:
    print("Invalid Choice")