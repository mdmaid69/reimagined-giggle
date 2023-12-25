  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def greet(name):
        print(f"Hello, {name}!")