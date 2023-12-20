import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()