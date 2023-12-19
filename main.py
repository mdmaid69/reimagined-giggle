import datetime
def get_current_date():
        return datetime.date.today()
import glob
def find_files(pattern):
        return glob.glob(pattern)