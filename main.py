  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_pressure(force, area):
        return force / area