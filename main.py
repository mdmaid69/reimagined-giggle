  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)