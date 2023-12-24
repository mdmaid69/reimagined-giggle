  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5