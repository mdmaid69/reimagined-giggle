import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import sys
  def get_python_version():
        return sys.version