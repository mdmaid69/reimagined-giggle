import getpass
def get_username():
        return getpass.getuser()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)