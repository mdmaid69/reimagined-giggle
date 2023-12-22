import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"