  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_volume(length, width, height):
        return length * width * height