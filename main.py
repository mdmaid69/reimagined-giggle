import datetime
print(datetime.datetime.now())
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()