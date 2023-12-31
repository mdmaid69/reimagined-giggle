  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)