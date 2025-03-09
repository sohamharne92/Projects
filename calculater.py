# Simple Calculator in Python with continuous operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Prompt user to input choice of operation
    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if choice is valid
    if choice in ['1', '2', '3', '4']:
        # Prompt user to input two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Error! Division by zero.")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input")
