import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import datetime
def get_today_date():
        return datetime.date.today()