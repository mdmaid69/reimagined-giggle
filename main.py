import collections
def create_user_list():
        return collections.UserList()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)