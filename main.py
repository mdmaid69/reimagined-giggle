import getpass
def get_username():
        return getpass.getuser()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])