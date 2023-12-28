import os
def list_files_in_directory(path):
        return os.listdir(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread