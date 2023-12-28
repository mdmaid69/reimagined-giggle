import platform
def get_python_version():
        return platform.python_version()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread