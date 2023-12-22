import json
def convert_to_json(data):
        return json.dumps(data)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)