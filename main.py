def find_difference(list1, list2):
        return set(list1) - set(list2)
import shutil
def delete_directory(path):
        shutil.rmtree(path)