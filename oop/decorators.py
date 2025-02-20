# Topic: OOP | Decorators
import time


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles ✨")
        time.sleep(1)
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge 🍫")
        time.sleep(1)
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍧")


get_ice_cream("vanilla")
