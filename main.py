  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)