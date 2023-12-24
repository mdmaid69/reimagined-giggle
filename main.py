import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import os
def get_environment_variable(var):
        return os.getenv(var)