import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])