  def convert_to_hex(n):
        return hex(n)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)