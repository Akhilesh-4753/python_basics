#1 Positive or negative or zero

user_number = input("Write any number :")

if user_number > "0":
    print("it is a positive number")
elif user_number < "0":
    print("it is a negative number")
else:
    print("it is Zero")

# -------------------------------------------------------------------------------#

# Even or Add

user_number = input("Enter your number : ")
even_number = int(user_number) % 2 == 0

if even_number:
    print("It is even number")
else:
    print("It is odd number")

# -------------------------------------------------------------------------------#

# Largest number based on user input

array_numbers = []

for i in range(3):
    number = int(input("Enter three number : "))
    array_numbers.append(number)

largest_number = 0

for num in array_numbers:

    if num > largest_number:
        largest_number = num
print(f"Largest number is : {largest_number}")
