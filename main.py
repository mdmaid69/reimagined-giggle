  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import platform
def get_python_version():
        return platform.python_version()