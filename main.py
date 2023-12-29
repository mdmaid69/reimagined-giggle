numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)