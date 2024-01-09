import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def remove_duplicates(lst):
        return list(set(lst))