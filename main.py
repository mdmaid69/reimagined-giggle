import random
def generate_random_number(start, end):
        return random.randint(start, end)
import platform
def get_os_info():
        return platform.uname()