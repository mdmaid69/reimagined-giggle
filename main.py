import getpass
def get_username():
        return getpass.getuser()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])