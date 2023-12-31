  import sqlite3
  def close_database_connection(connection):
        connection.close()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)