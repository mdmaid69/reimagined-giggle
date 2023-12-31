import sys
def add_to_python_path(path):
        sys.path.append(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread