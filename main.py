def remove_duplicates(lst):
        return list(set(lst))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)