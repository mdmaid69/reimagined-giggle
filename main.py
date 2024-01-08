import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)