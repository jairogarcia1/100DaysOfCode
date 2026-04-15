from Crypto.Random.random import choice
from azure.cli.command_modules.netappfiles.custom import calculate_oracle_throughput
from orca import mathsymbols

import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    print(" +\n", "-\n", "*\n", "/\n")
    num1 = float(input("Enter first number: "))
    mathsymbol = input("Pick an operation:  ")
    num2 = float(input("Enter second number: "))

    should_accumulate = True
    while should_accumulate:
        if mathsymbol in operations:
            operation = operations[mathsymbol]
            result = operation(num1, num2)
            print(f"{num1} {mathsymbol} {num2} = {result}")
            choice = input(f"Press 'y' to continue calculating with {result} or press 'n' to quit.")
            if choice == "y":
                print(" +\n", "-\n", "*\n", "/\n")
                mathsymbol = input("Pick an operation:  ")
                num1 = result
                num2 = float(input("Enter next number: "))
            else:
                should_accumulate = False
                print("\n" * 20)
                calculator()

        else:
            print("Invalid operation")

calculator()