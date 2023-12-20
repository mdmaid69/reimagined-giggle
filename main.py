import os
def change_working_directory(path):
        os.chdir(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread