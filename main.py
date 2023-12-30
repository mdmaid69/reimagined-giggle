import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import random
def roll_die():
        return random.randint(1, 6)