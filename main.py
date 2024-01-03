import getpass
def get_username():
        return getpass.getuser()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)