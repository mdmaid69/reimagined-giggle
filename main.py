import time
def get_time_since_epoch():
        return time.time()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)