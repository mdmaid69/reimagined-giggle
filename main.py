import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import random
def roll_die():
        return random.randint(1, 6)