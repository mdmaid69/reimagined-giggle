import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)