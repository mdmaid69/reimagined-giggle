import os
def get_environment_variable(var):
        return os.getenv(var)
import datetime
def get_today_date():
        return datetime.date.today()