
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
        