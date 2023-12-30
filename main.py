import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])