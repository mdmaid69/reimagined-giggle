n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import collections
def create_user_string():
        return collections.UserString()