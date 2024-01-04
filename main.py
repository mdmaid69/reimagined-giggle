import random
def generate_random_number(start, end):
        return random.randint(start, end)
import os
def get_environment_variable(var):
        return os.getenv(var)