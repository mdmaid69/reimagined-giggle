import os
def remove_directory(path):
        os.rmdir(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread