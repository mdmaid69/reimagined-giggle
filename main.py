import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())