n = 10
print("Powers of 2:", [2**x for x in range(n)])
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)