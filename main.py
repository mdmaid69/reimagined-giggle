import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"