
name = input("\nWhat is your name: ")

def greeting():
    print("\nHi There! " + name)
    print("I hope you've had a decent day today...")

print("\n\n------------Greeting Function---------------\n")
greeting()

# Programmer: Jordyn Kuhn
# Date: 12.16.19
# Program: Guess My Number

myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number
# until it is equal to my number
while guess != myNumber:
    print("\nNope, guess again")
    guess = int(input("\n\nEnter a Guess: "))

print("\nCongratulations! You have guessed the number!\n\n")


# Programmer: Jordyn Kuhn
# Date: 12.19.19
# Program: 1 Through 10


x = 1

# While loop will see if a condition has been met
# If it not it will run again until the condition has been met

while x <= 10:
    print(x)
    x += 1

# Programmer: Jordyn Kuhn
# Date: 1.6.20
# Program: Running Total, Part II

# This program asks users for 5 numbers,
# it then sums up the numbers.


sum = 0
howManyNumbers = int(input("\nHow many numbers would you like to sum up: "))
print("")

for i in range(howManyNumbers):
    enter_a_number = int(input("Enter A Number: "))
    sum = sum + enter_a_number

print("\nThe Sum of Your Numbers: " + str(sum))


# Programmer: Jordyn Kuhn
# Date: 1.7.20
# Program: Average Test Scores

# This program asks users how many tests they want to
# average.

total = 0
numOfTests = int(input("\nHow many tests are you averaging: "))
print("")

for i in range(numOfTests):
    enterScore = float(input("Enter the test score: "))
    total = total + enterScore

average = (total/numOfTests)

print("\nYour average is " + str(round(average, 2)))

# Programmer: Jordyn Kuhn
# Program: 1.20.20
# Date: Double For Loop

for i in range(3):
    print("\nOuter For Loop " + str(i))
    for k in range(4):
        print("\tInner for loop " + str(k))

print("\n------------------------------\n")

# Programmer: Jordyn Kuhn
# Program: 1.21.20
# Date: While Loop Nested Inside of a For Loop

for i in range(4):
    print("For Loop: " + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
        x = x - 1


# Date: 2.3.20
# Programmer: Jordyn Kuhn

# Define Global Variables Here \/


x = 15

# Define Functions Here \/

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

