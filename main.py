numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()