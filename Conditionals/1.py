# Sample Complex Conditional Statement with Operators and Arithmetic Functions

# Get user input for three numbers, with additional arithmetic operations
x = float(input("Enter the first number: "))
y = float(input("Enter the second number to add to the first number: "))
z = float(input("Enter the third number to subtract from the previous result: "))

# Perform arithmetic operations
result = x + y - z

# Check multiple conditions using nested conditionals and operators
if result > x:
    if result > y:
        print("The result is greater than both the first and second numbers")
    elif result == y:
        print("The result is equal to the second number")
    else:
        print("The result is smaller than the second number")
elif result < x:
    if result > y:
        print("The result is greater than the second number")
    elif result == y:
        print("The result is equal to the second number")
    else:
        print("The result is smaller than both the first and second numbers")
else:
    print("The result is equal to the first number")

# Check if the result is positive or negative
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is zero")
