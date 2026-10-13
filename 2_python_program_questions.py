#1-Multiplication table based on user entered number

# entered_number = int(input("enter a number : "))

# for i in range(1,11):
#     multiplication = i * entered_number
#     print(f"{i} * {entered_number} = {multiplication}")

# -------------------------------------------------------------------------------#

#2-factorial number calculation based on given number

# factorial_number = 1
# i = 1

# number = int(input("Enter a number : "))

# while i<= number:
#     factorial_number *= i
#     i+=1
# print(factorial_number)

# -------------------------------------------------------------------------------#

#3-determine whether a given number is prime number

# number = int(input("Enter a number: "))

# if number <= 1:
#     print("Not a prime number")  
# else:
#     for i in range(2, number):
#         if number % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")   

# -------------------------------------------------------------------------------#

#4-Given an integer N, find and print the next prime number greater than N.

# number = int(input("Enter a number: "))

# number +=1

# while True:
#     for i in range(2,number):
#         if number % i == 0:
#             break
#     else:
#         print(f"next prime number is : {number}")
#         break

    # number +=1

#5-Print the first N terms of the Fibonacci sequence.

# number = int(input("Enter number: "))

# a = 0
# b = 1

# for i in range(number):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c


#6-Print all divisors of a given integer.

# number = int(input("Enter a number: "))

# for i in range(1,number+1):
#     if number % i == 0:
#         print(i,end=" ")

#7-Find the Greatest Common Divisor (GCD) of two numbers without using built-in functions.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# smaller = min(num1, num2)
# gcd = 1

# for i in range(1, smaller + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD =", gcd)

#8-Find the Least Common Multiple (LCM) of two numbers.

# number1 = int(input("enter first number : "))
# number2 = int(input("enter second number : "))

# lcm = max(number1,number2)

# while True:
#     if lcm % number1 == 0 and lcm % number2 == 0 :
#         print("LCM = ",lcm)
#         break

#     lcm += 1

#9-Count the total number of digits in a given integer.

# number = int(input("Enter a number: "))

# count = 0

# while number > 0:
#     number = number // 10
#     count += 1

# print("Total digits =", count)

#10-Reverse the digits of a given integer.

# number = int(input("Enter a number: "))

# reverse = 0

# while number > 0:
#     degit = number % 10
#     reverse = reverse * 10 + degit
#     number = number // 10

# print("Reversed number =", reverse)
