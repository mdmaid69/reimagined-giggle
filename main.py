import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()