import datetime
def get_current_datetime():
        return datetime.datetime.now()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()