import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())