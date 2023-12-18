import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
n = 10
print("Powers of 2:", [2**x for x in range(n)])