import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import os
def get_environment_variable(var):
        return os.getenv(var)