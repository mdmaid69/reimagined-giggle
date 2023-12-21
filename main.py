import random
print(random.randint(0, 100))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)