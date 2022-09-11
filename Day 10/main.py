from art import logo


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        # divide by 0 is not allowed. returning 0 for now
        return 0
    return num1 / num2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide,
}


def calculator():
    calculate = True
    print(logo)
    num1 = float(input("Whats the first number: "))
    for key in operations:
        print(key)

    while calculate:
        user_operation = input("Pick an operation: ")
        num2 = float(input("Whats the next number: "))
        calc_fun = operations[user_operation]
        answer = calc_fun(num1, num2)

        print(f"{num1} {user_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            calculate = False
            calculator()


calculator()
