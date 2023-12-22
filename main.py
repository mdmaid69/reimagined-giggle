n = 10
print("Square numbers:", [x**2 for x in range(n)])
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)