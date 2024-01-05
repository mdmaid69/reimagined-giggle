import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def greet(name):
        print(f"Hello, {name}!")