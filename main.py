  import sys
  def get_python_version():
        return sys.version
import re
def split_string(pattern, string):
        return re.split(pattern, string)