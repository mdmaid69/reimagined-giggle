print(sum(range(10)))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)