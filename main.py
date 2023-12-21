import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"