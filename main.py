import collections
def create_user_list():
        return collections.UserList()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])