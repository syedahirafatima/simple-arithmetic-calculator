# My simple arithmetic calculator - public

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def calculator():
    print("Simple Arithmetic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please choose from 1 to 4.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# for running the calculator
calculator()
