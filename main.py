  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
def calculate_energy(mass, c=3*10**8):
        return mass * c**2