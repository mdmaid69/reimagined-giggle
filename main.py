import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list