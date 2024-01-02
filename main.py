import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import random
def roll_die():
        return random.randint(1, 6)