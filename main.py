import platform
def get_os_info():
        return platform.uname()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"