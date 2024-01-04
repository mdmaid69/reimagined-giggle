import time
def get_current_time():
        return time.ctime()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()