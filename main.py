  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import os
def get_environment_variable(var):
        return os.getenv(var)