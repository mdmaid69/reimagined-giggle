import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)