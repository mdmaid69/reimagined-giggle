  import sys
  def get_python_version():
        return sys.version
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)