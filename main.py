  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)