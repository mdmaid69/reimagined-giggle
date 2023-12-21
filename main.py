import random
def roll_die():
        return random.randint(1, 6)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()