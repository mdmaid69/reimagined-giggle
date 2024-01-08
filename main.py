import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"