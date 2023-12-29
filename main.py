  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value