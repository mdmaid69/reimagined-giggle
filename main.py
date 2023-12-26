import shutil
def delete_directory(path):
        shutil.rmtree(path)
import time
def get_time_since_epoch():
        return time.time()