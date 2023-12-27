  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"