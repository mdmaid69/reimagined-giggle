import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
text = "Hello, world!"
print("Reversed:", text[::-1])