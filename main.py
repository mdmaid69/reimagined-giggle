import sys
def add_to_python_path(path):
        sys.path.append(path)
import random
def roll_die():
        return random.randint(1, 6)