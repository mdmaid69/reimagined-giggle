import platform
def get_python_version():
        return platform.python_version()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"