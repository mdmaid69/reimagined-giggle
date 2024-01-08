import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b