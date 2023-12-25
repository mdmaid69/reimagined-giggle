import collections
def create_user_dict():
        return collections.UserDict()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b