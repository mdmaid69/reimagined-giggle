import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import time
def get_current_time():
        return time.ctime()