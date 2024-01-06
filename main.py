  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)