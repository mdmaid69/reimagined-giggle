import os
def get_file_size(filename):
        return os.path.getsize(filename)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread