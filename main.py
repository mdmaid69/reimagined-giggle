  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)