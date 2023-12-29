import json
def read_from_json(json_string):
        return json.loads(json_string)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)