import art

def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts a number from another"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies one number by another"""
    return n1 * n2

def divide(n1, n2):
    """Divides a number by another"""
    return n1 / n2

def print_ops():
    for ops in operations:
        print(ops)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    continueCalc = True
    n1 = float(input("What's the first number?: "))
    continueCalc = "y"
    while continueCalc == 'y':
        print_ops()
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            n1 = result 
        else:
            continueCalc = False
            print("\n" * 20)
            calculator()

calculator()
