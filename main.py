import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def find_difference(list1, list2):
        return set(list1) - set(list2)