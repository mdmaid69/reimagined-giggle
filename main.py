import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import re
print(re.match("h.*o", "hello world"))