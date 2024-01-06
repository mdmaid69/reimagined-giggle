  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"