def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt user to choose an operation
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Ensure valid operation is chosen
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        return
    
    # Prompt user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform the chosen operation
    if operation == '1':
        result = num1 + num2
        operator = '+'
    elif operation == '2':
        result = num1 - num2
        operator = '-'
    elif operation == '3':
        result = num1 * num2
        operator = '*'
    elif operation == '4':
        if num2 == 0:
            print("Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = '/'
    
    # Display the result
    print(f"Result: {num1} {operator} {num2} = {result}")

# Run the calculator
calculator()