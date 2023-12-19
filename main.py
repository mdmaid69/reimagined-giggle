import sys
print(sys.version)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)