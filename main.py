import getpass
def get_username():
        return getpass.getuser()
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)