def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"