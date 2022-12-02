def decorator_example(func):
    print("Decorator called")

    def inner_function(*args, **kwargs):
        print("Calling the function")
        func(*args, **kwargs)
        print("Function's execution is over")

    return inner_function


@decorator_example
def some_function():
    print("Executing the function")
    # Function logic goes here
