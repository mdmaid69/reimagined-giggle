import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import os
def list_files_in_directory(path):
        return os.listdir(path)