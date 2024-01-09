import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)