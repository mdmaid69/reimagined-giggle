import sys
def add_to_python_path(path):
        sys.path.append(path)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"