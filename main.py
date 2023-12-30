import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
print("Hello, world!")