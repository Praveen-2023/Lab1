"""This script contains basic programs for numerical and geometric calculations."""

# A program to check if a number is positive, negative, or zero

NUMBER = 85986
if NUMBER > 0:
    print("The number is positive.")
elif NUMBER < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# A program to find the largest of two numbers

NUM1 =6865
NUM2 = 5676

if NUM1 > NUM2:
    LARGEST = NUM1
else:
    LARGEST = NUM2

print("The largest number is:", LARGEST)

# A program to find Area of a rectangle
LENGTH = 356
WIDTH = 980
AREA1 = LENGTH * WIDTH
print("The area of the rectangle is:", AREA1)

# A program to find Area of a rectangle

RADIUS = 698
AREA2 = 3.14 * RADIUS**2
print("The area of the circle is:", AREA2)

# A program to check if a word is a palindrome

WORD = "kjbch"
if WORD == WORD[::-1]:
    print(f"{WORD} is a palindrome.")
else:
    print(f"{WORD} is not a palindrome.")
