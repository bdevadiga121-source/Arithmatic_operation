num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator to be used(+,-,/,*): ")


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '/':
    if num2 == 0:
        print("Division operation cannot be obtained")
        result = None
    else:
        result =num1/num2
elif operator == '*':
    result = num1 * num2
else:
    print("Invalid operator")
    result = None



if result is not None:
    print("Result: ",result)

    if result > 0:
        print("Result is positive")

    if result < 0:
        print("Result is negative")
    else:
        print("Result is zero")

    if result >= 0 and result <= 100:
        print("The result is between 0 to 100 range")

    if result <0 and result >100:
        print("The result is outside the 0 to 100 range ")

    if not result == 0:
        print("The result is non-zero")

