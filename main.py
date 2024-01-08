  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)