import datetime
def get_current_date():
        return datetime.date.today()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()