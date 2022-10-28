import time


def speed_calc_decorator(function):
    def wrapper_func():
        before_time = time.time()
        function()
        after_time = time.time()
        runtime = after_time - before_time
        func_name = function.__name__
        print(f"{func_name} run speed is: {runtime}")
    return wrapper_func


@speed_calc_decorator
def fast_function():
    for i in range(100_000_00):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100_000_000):
        i * i


fast_function()
slow_function()
