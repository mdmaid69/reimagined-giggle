import random
def generate_random_choice(choices):
        return random.choice(choices)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()