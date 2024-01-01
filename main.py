import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list