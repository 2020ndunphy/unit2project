def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

equation = input("Choose 1(multiplication) or 2(addition):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if equation == "1":
    print(num1, "*", num2, "=", multiply(num1,num2))


elif equation == "2":
    print(num1, "+", num2, "=", add(num1,num2))
else:
    print("That is not a math function. Try Again.")
