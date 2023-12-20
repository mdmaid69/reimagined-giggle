import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()