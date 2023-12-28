import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def remove_duplicates(lst):
        return list(set(lst))