def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()