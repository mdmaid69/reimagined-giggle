import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def find_union(list1, list2):
        return set(list1) | set(list2)