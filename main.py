import collections
def create_user_dict():
        return collections.UserDict()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)