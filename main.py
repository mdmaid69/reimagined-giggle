import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import time
def get_time_since_epoch():
        return time.time()