  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets