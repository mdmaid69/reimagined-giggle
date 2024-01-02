import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)