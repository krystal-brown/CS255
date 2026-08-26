def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Welcome to the calculator!")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    else:
        result = "Invalid operation."

    print("Result:", result)

if __name__ == "__main__":
    main()

