import collections
def create_user_list():
        return collections.UserList()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b