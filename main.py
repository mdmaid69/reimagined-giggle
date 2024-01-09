import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import platform
def get_os_info():
        return platform.uname()