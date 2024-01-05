def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"