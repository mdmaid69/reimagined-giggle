import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def find_difference(list1, list2):
        return set(list1) - set(list2)