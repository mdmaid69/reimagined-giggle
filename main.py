import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import sys
def print_python_version():
        print(sys.version)