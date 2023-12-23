import shutil
def delete_directory(path):
        shutil.rmtree(path)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)