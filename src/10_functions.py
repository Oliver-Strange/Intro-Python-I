# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def evenNum(num):
    if (num % 2) == 0:
        return True


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# print(evenNum(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def evenOdd(num):
    if (num % 2) == 0:
        print('Even!')
    else:
        print("Odd")


print(evenOdd(num))
