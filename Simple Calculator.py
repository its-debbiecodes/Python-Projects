
def add(a:float, b:float) -> float:
    """return the sum of two numbers"""
    return a+b

def subtract(a:float, b:float) -> float:
    """return the difference of two numbers"""
    return a-b

def multiply(a:float, b:float) -> float:
    """return the product of two numbers"""
    return a*b

def divide(a:float, b:float) -> float:
    """return the quotient of two numbers, division by zero error"""
    if b==0:
        raise ZeroDivisionError("division by zero is not allowed")
    return a/b

def modulo(a:float, b:float) -> float:
    """return the percentage of two numbers"""
    return a%b

def power(a:float, b:float) -> float:
    """return the power of two numbers"""
    return a**b

def get_number(prompt:str) -> float:
    """ensures input is a valid number"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value")

#dictionary for operations
def main():
    print("---Welcome to the Simple Calculator---")
    operations= {
        "+" : add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulo,
        "^": power,
    }
#Getting user's input
    while True:
        num_1 = get_number("Please enter your first number: ")
        op_symbol = input("Please enter your operation \nAvailable operations: \n+ Add \n- Subtract \n* Multiply \n/ Divide \n% Modulo \n^ power ")
        calculation_function = operations.get(op_symbol)
        num_2 = get_number("Please enter your second number: ")


#Calculation results
        if calculation_function:
            try:
                result = calculation_function(num_1, num_2)
                print(f"\nresult: {num_1} {op_symbol} {num_2}= {result}")
            except ZeroDivisionError as e:
                print(f"error:  {e}")

        else:
            print("\nInvalid operator please use (+,-,* or /) ")

#play again? function for user
        run_again = input("\nDo you wish to continue? (y/n): ")
        if run_again != "y" and run_again != "yes":
            print("Thank you for using the Simple Calculator!")
            break

if __name__ == "__main__":
    main()