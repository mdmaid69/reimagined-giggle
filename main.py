import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list