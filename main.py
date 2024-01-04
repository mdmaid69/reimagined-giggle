  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)