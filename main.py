import sys
def add_to_python_path(path):
        sys.path.append(path)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)