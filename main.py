import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])