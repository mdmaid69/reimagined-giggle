import platform
def get_os_info():
        return platform.uname()
import random
def generate_random_choice(choices):
        return random.choice(choices)