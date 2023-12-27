import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)