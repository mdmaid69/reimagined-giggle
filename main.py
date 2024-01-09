import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def count_elements(lst):
        return len(lst)