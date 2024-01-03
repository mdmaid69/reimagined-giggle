import collections
def create_user_dict():
        return collections.UserDict()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)