import datetime
def get_today_date():
        return datetime.date.today()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)