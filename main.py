import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)