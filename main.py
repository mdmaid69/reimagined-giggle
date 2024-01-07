import datetime
def get_current_date():
        return datetime.date.today()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)