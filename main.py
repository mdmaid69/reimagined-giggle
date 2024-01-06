import time
def get_current_time():
        return time.time()
import shutil
def delete_directory(path):
        shutil.rmtree(path)