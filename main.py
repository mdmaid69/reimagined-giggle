def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)