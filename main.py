import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)