num1 = int(input("Enter the value of first number: "))
num2 = int(input("Enter the value of second number: "))

print(num1)
print(num2)

operation = input("Enter an operation +, -, *, /")
if operation == "+":
    print(num1 +num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)