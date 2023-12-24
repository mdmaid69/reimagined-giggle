import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))