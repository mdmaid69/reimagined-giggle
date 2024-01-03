import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])