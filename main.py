import tensorflow as tf
print(tf.__version__)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list