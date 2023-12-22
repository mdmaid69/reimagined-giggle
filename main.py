  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)