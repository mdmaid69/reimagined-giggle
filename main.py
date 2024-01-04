text = "Hello, world!"
print("Words:", len(text.split()))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)