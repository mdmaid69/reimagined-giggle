n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)