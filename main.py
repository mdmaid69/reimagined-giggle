import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))