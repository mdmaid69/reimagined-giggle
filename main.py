import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)