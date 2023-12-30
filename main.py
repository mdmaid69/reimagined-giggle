import getpass
def get_username():
        return getpass.getuser()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"