
# Date: 2.3.20
# Programmer: Jordyn Kuhn

# Define Global Variables Here \/

name = input("\nWhat is your name: ")
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
    print("\nFirst Parameter Or Number: " + str(x))
    print("\nSecond Parameter Or Number: " + str(y))

# Print Sum \/


def printSum(x, y):
    print(x + y)

# Print Multiple Times\/


def printMultipleTimes(string, times):
    for i in range(times):
        print("\n" + string)


# Call Functions Here \/

print("\n\n------------Greeting Function---------------\n")
greeting()


print("\n\n------------Print Something Function---------------\n")
printSomething()
print(x)

print("\n\n------------Print Age Function---------------\n")

printNumber(28)
printNumber(39)

print("\n\n------------Print 2 Numbers Function---------------")
printTwoNumbers(23, 78)
printTwoNumbers(45)

print("\n\n------------Print the Sum of Two Numbers Function---------------\n")
printSum(136, 179)

print("\n\n------------Print Multiple Times Function---------------\n")
printMultipleTimes("I Love Computer Science", 15)

print("\n\nThat was quite a few functions...\n\n\n\n")
