import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)