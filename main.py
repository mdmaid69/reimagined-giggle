import getpass
def get_username():
        return getpass.getuser()
n = 10
print("Square numbers:", [x**2 for x in range(n)])