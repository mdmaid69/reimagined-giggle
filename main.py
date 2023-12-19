  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5