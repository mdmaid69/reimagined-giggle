  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2