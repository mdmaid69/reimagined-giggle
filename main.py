import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"