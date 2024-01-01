import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()