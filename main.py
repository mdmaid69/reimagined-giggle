import datetime
def get_current_date():
        return datetime.date.today()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)