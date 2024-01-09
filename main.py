import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)