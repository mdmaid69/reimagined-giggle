for i in range(5):
        print(i)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)