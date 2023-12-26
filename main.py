import datetime
def get_today_date():
        return datetime.date.today()
import os
def get_environment_variable(var):
        return os.getenv(var)