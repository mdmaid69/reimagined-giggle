import os
def get_environment_variable(var):
        return os.getenv(var)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list