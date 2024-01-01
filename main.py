import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import random
def generate_random_number(start, end):
        return random.randint(start, end)