import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import datetime
def get_today_date():
        return datetime.date.today()