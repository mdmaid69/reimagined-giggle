import platform
def get_python_version():
        return platform.python_version()
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)