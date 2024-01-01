import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import random
def generate_random_number(start, end):
        return random.randint(start, end)