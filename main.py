import time
def get_current_time():
        return time.ctime()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)