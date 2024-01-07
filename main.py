import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def greet(name):
        print(f"Hello, {name}!")