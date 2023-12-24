import platform
def get_os_info():
        return platform.uname()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"