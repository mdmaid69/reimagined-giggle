import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import sys
  def get_python_version():
        return sys.version