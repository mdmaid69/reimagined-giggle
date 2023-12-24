  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)