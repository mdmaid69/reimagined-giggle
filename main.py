import getpass
def get_username():
        return getpass.getuser()
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])