import datetime
def get_today_date():
        return datetime.date.today()
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"