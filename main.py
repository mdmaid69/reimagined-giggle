n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)