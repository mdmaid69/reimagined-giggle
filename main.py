import platform
def get_os_info():
        return platform.uname()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"