import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"