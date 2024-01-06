import random
print(random.randint(0, 100))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()