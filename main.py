import platform
def get_python_version():
        return platform.python_version()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"