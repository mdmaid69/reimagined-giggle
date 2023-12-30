import collections
def create_user_dict():
        return collections.UserDict()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])