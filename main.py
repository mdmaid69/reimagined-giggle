import random
def generate_random_choice(choices):
        return random.choice(choices)
import os
def get_environment_variable(var):
        return os.getenv(var)