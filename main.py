import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def find_union(list1, list2):
        return set(list1) | set(list2)