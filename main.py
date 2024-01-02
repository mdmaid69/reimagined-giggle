def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import glob
def find_files(pattern):
        return glob.glob(pattern)