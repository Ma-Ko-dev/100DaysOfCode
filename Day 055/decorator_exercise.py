def logging_decorator(function):
    def wrapper(*args):
        print(f"You called: {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
        function(*args)
    return wrapper


@logging_decorator
def add(*args):
    total = 0
    for num in args:
        total += num
    return total


add(1, 2, 3, 4, 5)
