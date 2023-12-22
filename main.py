import sys
print(sys.version)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)