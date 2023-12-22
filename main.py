  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity