def decorator_example(func):
    print("Decorator called")

    def inner_function(*args, **kwargs):
        print("Calling the function")
        # func(*args, **kwargs)
        print("Function's execution is over")

    return inner_function


@decorator_example
def some_function():
    print("Executing the function")
    # Function logic goes here


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper