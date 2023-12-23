import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"