import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import os
def get_current_working_directory():
        return os.getcwd()