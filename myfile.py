def greetingpeople(name):
    return f"Hello, {name}!"

def num_even(num):
    return num % 2 == 0

# setting up an intentional error
def find_maximum(a, b):
    if a < b:  # this should be a > b
        return a
    return b
