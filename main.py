import platform
def get_python_version():
        return platform.python_version()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())