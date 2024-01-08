import json
print(json.dumps({"name": "John", "age": 30}))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)