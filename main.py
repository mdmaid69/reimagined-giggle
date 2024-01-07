import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import time
print(time.time())