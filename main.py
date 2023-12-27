import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import random
def roll_die():
        return random.randint(1, 6)