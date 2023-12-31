import platform
def get_os_info():
        return platform.uname()
import random
def roll_die():
        return random.randint(1, 6)