import platform
def get_os_info():
        return platform.uname()
import datetime
def get_current_datetime():
        return datetime.datetime.now()