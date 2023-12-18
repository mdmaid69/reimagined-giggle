import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"