import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()