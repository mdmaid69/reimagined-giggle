import platform
def get_os_info():
        return platform.uname()
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)