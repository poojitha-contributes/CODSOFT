def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def calculator():
    print("Simple Calculator")

    # Prompt user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Prompt user to choose an operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation (1/2/3/4): ")

    # Perform the chosen operation
    if operation == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operation choice! Please choose 1, 2, 3, or 4.")


if __name__ == '__main__':
    calculator()
