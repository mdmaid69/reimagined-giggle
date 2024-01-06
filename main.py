  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import os
def get_environment_variable(var):
        return os.getenv(var)