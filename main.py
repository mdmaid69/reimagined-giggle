import random
def generate_random_number(start, end):
        return random.randint(start, end)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)