import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import os
print(os.getcwd())