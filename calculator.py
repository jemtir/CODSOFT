# Simple Calculator Program

def arithmetic_calculation():
    # Input two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Choose operation
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter choice (1/2/3/4): ")

        # Step 3: Perform calculation
        if choice == '1':
            result = num1 + num2
            print(f"\nResult: ({num1}) + ({num2}) = ({result})")

        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: ({num1}) - ({num2}) = ({result})")

        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: ({num1}) * ({num2}) = ({result})")

        elif choice == '4':
            # Check for division by zero
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: ({num1}) / ({num2}) = ({result})")
            else:
                print("\nError: Division by zero is not allowed.")

        else:
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")

    except ValueError:
        print("\nInvalid input! Please enter numeric values.")


# Run the function
arithmetic_calculation()
