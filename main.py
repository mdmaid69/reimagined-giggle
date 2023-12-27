  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)