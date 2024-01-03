import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def get_list_from_array(array):
        return array.tolist()