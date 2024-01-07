import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)