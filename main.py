import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])