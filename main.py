n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import getpass
def get_username():
        return getpass.getuser()