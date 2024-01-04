import sys
print(sys.version)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()