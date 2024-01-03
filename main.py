import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import shutil
def delete_directory(path):
        shutil.rmtree(path)