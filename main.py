def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)