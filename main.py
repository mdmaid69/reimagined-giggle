import sys
def print_python_version():
        print(sys.version)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"