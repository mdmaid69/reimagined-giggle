import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"