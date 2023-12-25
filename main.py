def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"