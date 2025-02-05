# A program to check if a number is positive, negative, or zero


number = 85986


if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# A program to find the largest of two numbers


num1 =6865
num2 = 5676


if num1 > num2:
    largest = num1
else:
    largest = num2


print("The largest number is:", largest)


# A program too fing Area of a rectangle


length = 356
width = 980
area = length * width


print("The area of the rectangle is:", area)


# A program too fing Area of a rectangle


radius = 698
area = 3.14 * radius**2
print("The area of the circle is:", area)


# A program to check if a word is a palindrome


word = "kjbch"
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")