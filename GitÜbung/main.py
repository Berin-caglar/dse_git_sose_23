#Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("Simple Calculator")
print("-----------------")

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Calculator exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid choice. Please try again.")

    print("-----------------")
