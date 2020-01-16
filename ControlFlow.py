
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

