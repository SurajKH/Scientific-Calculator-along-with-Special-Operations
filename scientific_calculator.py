import math


def addition(num1, num2):
    val = num1 + num2
    return val


def subtraction(num1, num2):
    val = num1 - num2
    return val


def multiplication(num1, num2):
    val = num1 * num2
    return val


def division(num1, num2):
    val = num1 / num2
    return val


# Now we consider other operations as well by considering the math librabry over here
def square_root(num1):
    val = math.sqrt(num1)
    return val


def exponent(num1):
    val = num1 ** 2
    return val


def sin_function(num1):
    val = math.sin(num1)
    return val


def cos_function(num1):
    val = math.cos(num1)
    return val


def tan_function(num1):
    val = math.tan(num1)
    return val


print("***********Scientific Calculator***********")

print("The Operations in Scientific Calculator are as followed")
print("1.Addition,2.subtraction,3.multiplication,4.division,5.square root,6.exponent,7.sin(x),8.cos(x),9.tan(x)")

option = int(input("Enter the operation to be performed: "))
if option == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = addition(num1, num2)
    print("The Result is: ", val)

if option == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = subtraction(num1, num2)
    print("The Result is: ", val)

if option == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = multiplication(num1, num2)
    print("The Result is: ", val)

if option == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = division(num1, num2)
    print("The Result is: ", val)

if option == 5:
    num1 = int(input("Enter the number: "))
    val = square_root(num1)
    print("The Result is: ", val)

if option == 6:
    num1 = int(input("Enter the  number: "))
    val = exponent(num1)
    print("The Result is: ", val)

if option == 7:
    num1 = int(input("Enter the number: "))
    val = sin_function(num1)
    print("The Result is: ", val)

if option == 8:
    num1 = int(input("Enter the  number: "))
    val = cos_function(num1)
    print("The Result is: ", val)

if option == 9:
    num1 = int(input("Enter the  number: "))
    val = tan_function(num1)
    print("The Result is: ", val)
