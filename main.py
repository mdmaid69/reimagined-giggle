i = 0
while i < 5:
        print(i)
        i += 1
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)