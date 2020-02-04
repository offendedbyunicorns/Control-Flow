
# Date: 2.3.20
# Programmer: Jordyn Kuhn

# Define Global Variables Here \/

# name = input("\nWhat is your name: ")
x = 15

# Define Functions Here \/

# Greeting Function \/


def greeting():
    print("\nHi There! " + name)
    print("I hope you've had a decent day today...")

# Functions & A Local Variable \/


def printSomething():
    x = 3
    print(x)

# Functions & Parameters \/
# Function Name = printNumber with a parameter of age \/


def printNumber(age):
    print(age)

# Default Parameter Values \/


def printTwoNumbers(x, y=71):
    print("First Parameter Or Number: " + str(x))
    print("Second Parameter Or Number: " + str(y))

# Call Functions Here \/


# greeting()
# printSomething()
# print(x)
# printNumber(28)
# printNumber(39)
printTwoNumbers(23, 78)
printTwoNumbers(45)