def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"