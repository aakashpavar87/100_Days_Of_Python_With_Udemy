from Art import logo

print(logo)
print("Welcome to the python Calculator and enter your two Numbers !")

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2
def calculator():
    calc = {"*": multiply, "/": divide, "+": add, "-": substract}
    num1 = float(input("Enter Number 1 : "))
    for symbol in calc:
        print(f"{symbol}")
    should_continue = True
    while should_continue:
        choice = input("Choose operation from above : ")
        num2 = float(input("Enter Number 2 : "))
        function_name = calc[choice]
        result = function_name(n1=num1,n2=num2)
        print(f"Here, your Result of {num1} {choice} {num2} is {result}")
        decision = input(f"Type 'y' to continue with {result}, type 'n' to start a new calculation, or type 'END' for exit : ")
        if decision == "y":
            num1 = result
        elif decision == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False           
calculator()
    # num3 = int(input("Enter another number : "))
    # for symbol in calc:
    #     print(f"{symbol}")
    # choice = input("Choose operation from above : ")
    # new_function_name = calc[choice]
    # new_result = new_function_name(function_name(n1=num1,n2=num2),num3)
    # print(f"Here, your Result of {result} {choice} {num3} is {new_result}")
