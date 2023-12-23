import platform
def get_os_info():
        return platform.uname()
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)