import math
# Objectives
# root of an equation
def root_of_the_equation(a_1, b_1, c_1):
    root_1 = (-b_1 + math.sqrt(math.pow(b_1,2)-4*a_1*c_1)) / 2 * a_1
    root_2 = (b_1 + math.sqrt(math.pow(b_1,2)-4*a_1*c_1)) / 2 * a_1

    print("roots of the equation are as followed:\n")
    if root_1 == root_2:
        print("Root 1 is : ", root_1)
        print("Root 2 is : ", root_2)
        print("Roots are equal")
    else:
        print("Root 1 : ", root_1)
        print("Root 2 : ", root_2)


# factors of the resultant operation
def factors_of_number(number_1):
    item_list = []
    for i in range(1, number_1):
        if number_1 % i == 0:
            item_list.append(i)
    return item_list


# check if result is Prime or Not
def prime_or_not(number_1):
    flag = 1
    for i in range(2, number_1):
        if number_1 % i == 0:
            # print("The number is not Prime")
            flag = 0
            break
    if flag == 1:
        print("Its a Prime Number.")
    elif flag == 0:
        print("its Not a Prime Number.")

# addition function
def addition(number_1, number_2):
    value = number_1 + number_2
    return value


# subtraction function
def subtraction(number_1, number_2):
    value = number_1 - number_2
    return value


# multiplication function
def multiplication(number_1, number_2):
    value = number_1 * number_2
    return value


# division function
def division(number_1, number_2):
    value = number_1 / number_2
    return value


# Now we consider other operations as well by considering the math library over here
# square root of a number
def square_root(number_1):
    value = math.sqrt(number_1)
    return value


# exponent(num1) function
def exponent(number_1):
    value = number_1 ** 2
    return value


# sin(x) function
def sin_function(degree):
    value = math.sin(degree)
    return value


# cos(x) function
def cos_function(degree):
    value = math.cos(degree)
    return value


# tan(x) Function
def tan_function(degree):
    value = math.tan(degree)
    return value


print("***********Scientific Calculator***********")
print("\nThe Operations in Scientific Calculator\n")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square root of a Number\n6.exponent of a Number\n7.sin(x)\n8.cos(x)\n9.tan(x)\n10.Roots of equations\n11.Factors of a number\n12.Prime or Not\n")
option = int(input("Enter Your choice:\n"))
if option == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = addition(num1, num2)
    print("The Result of addition of two numbers is: ", val)
elif option == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = subtraction(num1, num2)
    print("The Result of subtraction of two numbers is: ", val)
elif option == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = multiplication(num1, num2)
    print("The Result is of multiplication of two numbers is: ", val)

elif option == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second number: "))
    val = division(num1, num2)
    print("The Result of division of two numbers is: ", val)
elif option == 5:
    num1 = int(input("Enter the number: "))
    val = square_root(num1)
    print("The Square root of a number is: ", val)
elif option == 6:
    num1 = int(input("Enter the  number: "))
    val = exponent(num1)
    print("The exponent of a number is as followed: ", val)
elif option == 7:
    num1 = int(input("Enter the number: "))
    val = sin_function(num1)
    print("The sin function of the number is: ", val)
elif option == 8:
    num1 = int(input("Enter the  number: "))
    val = cos_function(num1)
    print("The cos function of the number is: ", val)
elif option == 9:
    num1 = int(input("Enter the  number: "))
    val = tan_function(num1)
    print("The tan function of the number is: ", val)
elif option == 10:
    print("Enter the co-efficients for a and b for the quadratic equation:\n")
    a = int(input("Enter the first coefficient:\n"))
    b = int(input("Enter the second coefficient:\n"))
    c = int(input("Enter the constant value:\n"))
    root_of_the_equation(a,b,c)
elif option == 11:
    # print("Enter number:\n")
    number_1 = int(input("Enter the number to determine the factors:\n"))
    val_list = factors_of_number(number_1)
    for item in val_list:
        print(str(item)+" ")
elif option == 12:
    number_1 = int(input("Enter the number to determine whether it is prime or not:\n"))
    prime_or_not(number_1)
