import platform
def get_os_info():
        return platform.uname()
import time
def get_current_time():
        return time.ctime()