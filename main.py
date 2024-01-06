  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)