import collections
def create_user_list():
        return collections.UserList()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])