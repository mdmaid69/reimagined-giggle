import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])