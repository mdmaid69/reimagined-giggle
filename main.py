  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)