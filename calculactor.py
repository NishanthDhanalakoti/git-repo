num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    sum_result = num1 + num2
    print(f"The sum of the numbers is: {sum_result}")
elif operator == '-':
    diff = num1 - num2
    print(f"The difference of the numbers is: {diff}")
elif operator == '*':
    prod = num1 * num2
    print(f"The product of the numbers is: {prod}")
elif operator == '/':
    if num2 != 0:
        divi = num1 / num2
        print(f"The division of the numbers is: {divi}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Please enter a valid operator (+, -, *, /).")