import os
print(os.getcwd())
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)