import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list