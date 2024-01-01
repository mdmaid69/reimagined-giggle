import random
def generate_random_choice(choices):
        return random.choice(choices)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())