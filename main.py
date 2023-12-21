import sys
def add_to_python_path(path):
        sys.path.append(path)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"