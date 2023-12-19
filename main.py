import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)