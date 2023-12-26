import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
n = 10
print("Square numbers:", [x**2 for x in range(n)])