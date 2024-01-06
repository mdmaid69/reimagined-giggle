  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)