import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread