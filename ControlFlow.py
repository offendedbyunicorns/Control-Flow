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
