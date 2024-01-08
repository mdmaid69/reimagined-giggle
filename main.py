import collections
def create_user_string():
        return collections.UserString()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])