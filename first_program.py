# 1-Positive or negative or zero

user_number = input("Write any number :")

if user_number > "0":
    print("it is a positive number")
elif user_number < "0":
    print("it is a negative number")
else:
    print("it is Zero")

# -------------------------------------------------------------------------------#

# 2-Even or Add

user_number = input("Enter your number : ")
even_number = int(user_number) % 2 == 0

if even_number:
    print("It is even number")
else:
    print("It is odd number")

# -------------------------------------------------------------------------------#

# 3-Largest number based on user input

array_numbers = []

for i in range(3):
    number = int(input("Enter three number : "))
    array_numbers.append(number)

largest_number = 0

for num in array_numbers:

    if num > largest_number:
        largest_number = num
print(f"Largest number is : {largest_number}")

# -------------------------------------------------------------------------------#

# Find Leap year

year = int(input("Enter your Year : "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("This year is leap year")
else:
    print("Not leap year")

# -------------------------------------------------------------------------------#

# Calculator

def menu():

    print("-------------------Menu----------------------")

    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")

    print("---------------------------------------------")

menu()

user_choice = int(input("Enter your choice : "))

while user_choice > 4 or user_choice < 1:
    menu()
    print("Enter valid choice")
    user_choice = int(input("Enter your choice : "))

num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))

if user_choice == 1:
    result = num1+num2
    print(f"Result is : {result}")
elif user_choice == 2:
    result = num1-num2
    print(f"Result is : {result}")
elif user_choice == 3:
    result = num1*num2
    print(f"Result is : {result}")
else:
    result = num1/num2
    print(f"Result is : {result}")
