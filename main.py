  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import sys
def add_to_python_path(path):
        sys.path.append(path)