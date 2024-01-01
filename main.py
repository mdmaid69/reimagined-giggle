import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)