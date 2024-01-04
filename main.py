  def remove_duplicates(lst):
        return list(set(lst))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()