  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import os
def get_environment_variable(var):
        return os.getenv(var)